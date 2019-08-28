"""new table authors

Revision ID: 03466b541e6e
Revises: eddd60e465a5
Create Date: 2019-08-29 00:31:23.170385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03466b541e6e'
down_revision = 'eddd60e465a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('display_name', sa.String(length=128), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('middle_name', sa.String(length=50), nullable=True),
    sa.Column('pseudonym', sa.String(length=128), nullable=True),
    sa.Column('birth_year', sa.Integer(), nullable=True),
    sa.Column('death_year', sa.Integer(), nullable=True),
    sa.Column('nationality', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('post', sa.Column('author_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'post', 'author', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'post', type_='foreignkey')
    op.drop_column('post', 'author_id')
    op.drop_table('author')
    # ### end Alembic commands ###
