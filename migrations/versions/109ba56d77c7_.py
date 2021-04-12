"""empty message

Revision ID: 109ba56d77c7
Revises: 
Create Date: 2021-04-09 21:02:28.389921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '109ba56d77c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('enduser', sa.String(length=80), nullable=True),
    sa.Column('extra_details', sa.String(length=80), nullable=True),
    sa.Column('specs', sa.String(length=80), nullable=True),
    sa.Column('part', sa.String(length=80), nullable=True),
    sa.Column('vendor', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('item')
    # ### end Alembic commands ###
