"""stock table added, relationship with products added

Revision ID: 06cb1872bda8
Revises: b8d09ec499fb
Create Date: 2023-02-23 23:58:15.185776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06cb1872bda8'
down_revision = 'b8d09ec499fb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('qty', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('products', sa.Column('stock_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'products', 'stock', ['stock_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'products', type_='foreignkey')
    op.drop_column('products', 'stock_id')
    op.drop_table('stock')
    # ### end Alembic commands ###