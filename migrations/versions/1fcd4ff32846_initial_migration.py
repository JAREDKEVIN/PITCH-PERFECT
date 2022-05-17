"""Initial Migration

Revision ID: 1fcd4ff32846
Revises: 5f0d9f376a23
Create Date: 2022-03-08 18:52:45.271631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fcd4ff32846'
down_revision = '5f0d9f376a23'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(length=250), nullable=True))
    op.drop_column('user', 'firstname')
    op.drop_column('user', 'lastname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('lastname', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('firstname', sa.VARCHAR(length=250), autoincrement=False, nullable=True))
    op.drop_column('user', 'username')
    # ### end Alembic commands ###