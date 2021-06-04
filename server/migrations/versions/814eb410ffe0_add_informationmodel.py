"""add informationModel

Revision ID: 814eb410ffe0
Revises: 
Create Date: 2021-05-31 16:47:44.486624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '814eb410ffe0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('information',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('background', sa.String(length=128), nullable=False),
    sa.Column('organization', sa.String(length=128), nullable=False),
    sa.ForeignKeyConstraint(['username'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_information_username'), 'information', ['username'], unique=True)
    op.add_column('users', sa.Column('user_type', sa.String(length=10), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'user_type')
    op.drop_index(op.f('ix_information_username'), table_name='information')
    op.drop_table('information')
    # ### end Alembic commands ###
