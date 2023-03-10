"""created_at and updated_at added on providers table

Revision ID: 3fcbf0c85525
Revises: 8e7193efafe7
Create Date: 2023-02-27 19:04:01.731077

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fcbf0c85525'
down_revision = '8e7193efafe7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('providers', sa.Column('created_at', sa.DateTime(timezone=True), nullable=False))
    op.add_column('providers', sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('providers', 'updated_at')
    op.drop_column('providers', 'created_at')
    # ### end Alembic commands ###
