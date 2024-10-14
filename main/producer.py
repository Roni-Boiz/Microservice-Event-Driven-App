import pika, json

params = pika.URLParameters('amqp://guest:guest@rabbitmq:5672/')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def reconnect_channel():
    global params, connection, channel
    try:
        params = pika.URLParameters('amqp://guest:guest@rabbitmq:5672/')
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        return channel
    except pika.exceptions.AMQPConnectionError as e:
        print(f"Connection failed: {e}")
        return None

def publish(method, body):
    global channel
    if channel is None or channel.is_closed:
        channel = reconnect_channel()
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)