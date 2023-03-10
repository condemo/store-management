"""add ondelete CASCADE to all relationships

Revision ID: 3f8b425e3f76
Revises: 98d28aa8d274
Create Date: 2023-02-25 00:32:51.458075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f8b425e3f76'
down_revision = '98d28aa8d274'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('products_stock_id_fkey', 'products', type_='foreignkey')
    op.drop_constraint('products_category_id_fkey', 'products', type_='foreignkey')
    op.drop_constraint('products_brand_id_fkey', 'products', type_='foreignkey')
    op.create_foreign_key(None, 'products', 'products_category', ['category_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'products', 'brands', ['brand_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'products', 'stock', ['stock_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.create_foreign_key('products_brand_id_fkey', 'products', 'brands', ['brand_id'], ['id'])
    op.create_foreign_key('products_category_id_fkey', 'products', 'products_category', ['category_id'], ['id'])
    op.create_foreign_key('products_stock_id_fkey', 'products', 'stock', ['stock_id'], ['id'])
    # ### end Alembic commands ###
