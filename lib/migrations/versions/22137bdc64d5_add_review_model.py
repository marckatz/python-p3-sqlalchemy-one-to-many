"""Add Review Model

Revision ID: 22137bdc64d5
Revises: 7300de6c5b5d
Create Date: 2023-07-14 13:43:28.993405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22137bdc64d5'
down_revision = '7300de6c5b5d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('game_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['game_id'], ['games.id'], name=op.f('fk_reviews_game_id_games')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reviews')
    # ### end Alembic commands ###
