"""add recordModel

Revision ID: a713d15941bc
Revises: 814eb410ffe0
Create Date: 2021-05-31 21:46:19.073587

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a713d15941bc'
down_revision = '814eb410ffe0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('commit_time', sa.DateTime(), nullable=False),
    sa.Column('symptoms', sa.Text(), nullable=False),
    sa.Column('image_path', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['username'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_records_username'), 'records', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_records_username'), table_name='records')
    op.drop_table('records')
    # ### end Alembic commands ###
