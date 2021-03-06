"""empty message

Revision ID: 5d41c9163958
Revises: 783f2ffc432a
Create Date: 2018-02-27 18:00:17.308749

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '5d41c9163958'
down_revision = '783f2ffc432a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('evaluations', sa.Column('date', sa.Date(), nullable=False))
    op.drop_column('evaluations', 'month')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('evaluations', sa.Column('month', mysql.VARCHAR(length=16), nullable=False))
    op.drop_column('evaluations', 'date')
    # ### end Alembic commands ###
