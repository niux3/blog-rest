"""ajoute user aux posts

Revision ID: 260d89ef4520
Revises: b6e04a93c98a
Create Date: 2023-08-31 10:26:46.456480

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '260d89ef4520'
down_revision = 'b6e04a93c98a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog_posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('authors', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'account_users', ['authors'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blog_posts', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('authors')

    # ### end Alembic commands ###
