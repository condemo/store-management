"""product_listed table and relationships added

Revision ID: 293d0c4d7948
Revises: 6361ef94ac37
Create Date: 2023-02-27 20:11:07.592204

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '293d0c4d7948'
down_revision = '6361ef94ac37'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products_listed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['provider_orders.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.alter_column('products', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('products', 'brand_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('products', 'stock_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('provider_orders', sa.Column('approx_delivery_date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('provider_orders', 'approx_delivery_date')
    op.alter_column('products', 'stock_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('products', 'brand_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('products', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_table('products_listed')
    # ### end Alembic commands ###
