"""add title to posts

Revision ID: eddd60e465a5
Revises: fc9647c7fa3c
Create Date: 2019-08-29 00:16:22.033380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eddd60e465a5'
down_revision = 'fc9647c7fa3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('date_written', sa.String(length=256), nullable=True))
    op.add_column('post', sa.Column('title', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'title')
    op.drop_column('post', 'date_written')
    # ### end Alembic commands ###