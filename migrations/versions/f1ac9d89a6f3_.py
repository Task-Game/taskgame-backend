"""empty message

Revision ID: f1ac9d89a6f3
Revises: 51d71058f375
Create Date: 2020-07-20 13:39:21.964272

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'f1ac9d89a6f3'
down_revision = '51d71058f375'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Tarefa', 'recompensa')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Tarefa', sa.Column('recompensa', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    # ### end Alembic commands ###