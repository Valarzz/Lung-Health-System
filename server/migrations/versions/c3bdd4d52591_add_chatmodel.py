"""add chatModel

Revision ID: c3bdd4d52591
Revises: a713d15941bc
Create Date: 2021-06-02 19:29:10.589263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c3bdd4d52591'
down_revision = 'a713d15941bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('chat',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('record_id', sa.Integer(), nullable=False),
    sa.Column('receiver', sa.String(length=64), nullable=True),
    sa.Column('sender', sa.String(length=64), nullable=True),
    sa.Column('commit_time', sa.DateTime(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['receiver'], ['users.username'], ),
    sa.ForeignKeyConstraint(['record_id'], ['records.id'], ),
    sa.ForeignKeyConstraint(['sender'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_chat_receiver'), 'chat', ['receiver'], unique=False)
    op.create_index(op.f('ix_chat_record_id'), 'chat', ['record_id'], unique=False)
    op.create_index(op.f('ix_chat_sender'), 'chat', ['sender'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_chat_sender'), table_name='chat')
    op.drop_index(op.f('ix_chat_record_id'), table_name='chat')
    op.drop_index(op.f('ix_chat_receiver'), table_name='chat')
    op.drop_table('chat')
    # ### end Alembic commands ###
