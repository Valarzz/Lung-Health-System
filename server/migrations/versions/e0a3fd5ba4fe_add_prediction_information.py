"""add prediction information

Revision ID: e0a3fd5ba4fe
Revises: ef1915447194
Create Date: 2021-06-04 08:46:17.390683

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0a3fd5ba4fe'
down_revision = 'ef1915447194'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('records', sa.Column('height', sa.Integer(), nullable=False))
    op.add_column('records', sa.Column('left', sa.Integer(), nullable=False))
    op.add_column('records', sa.Column('name', sa.String(length=64), nullable=False))
    op.add_column('records', sa.Column('score', sa.Float(), nullable=False))
    op.add_column('records', sa.Column('top', sa.Integer(), nullable=False))
    op.add_column('records', sa.Column('width', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('records', 'width')
    op.drop_column('records', 'top')
    op.drop_column('records', 'score')
    op.drop_column('records', 'name')
    op.drop_column('records', 'left')
    op.drop_column('records', 'height')
    # ### end Alembic commands ###
