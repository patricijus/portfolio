"""empty message

Revision ID: 999fec5a9177
Revises: 
Create Date: 2022-12-16 18:54:26.392804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '999fec5a9177'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('production_line',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('internal_code', sa.String(), nullable=False),
    sa.Column('customer_code', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('production_line_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['product_category.id'], ),
    sa.ForeignKeyConstraint(['production_line_id'], ['production_line.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('customer_code'),
    sa.UniqueConstraint('internal_code'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product')
    op.drop_table('user')
    op.drop_table('production_line')
    op.drop_table('product_category')
    # ### end Alembic commands ###