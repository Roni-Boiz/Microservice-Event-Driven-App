"""empty message

Revision ID: 9de2d1bd017e
Revises: 164d474c50fc
Create Date: 2024-10-14 12:36:04.096442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9de2d1bd017e'
down_revision = '164d474c50fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('likes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('product', 'likes')
    # ### end Alembic commands ###
