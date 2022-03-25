"""empty message

Revision ID: 756d2bf1616f
Revises: 
Create Date: 2022-03-25 11:04:16.801011

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '756d2bf1616f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_TEST',
    sa.Column('user_email', sa.String(), nullable=False),
    sa.Column('user_name', sa.String(length=200), nullable=False),
    sa.Column('user_password', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('user_email')
    )
    op.drop_table('user')
    op.drop_table('user_detail')
    op.drop_table('user_test')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_test',
    sa.Column('user_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_name', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('user_password', mysql.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('user_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('user_detail',
    sa.Column('name', mysql.VARCHAR(length=40), nullable=True),
    sa.Column('user_password', mysql.INTEGER(), autoincrement=False, nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('user',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=200), nullable=False),
    sa.Column('content', mysql.TEXT(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('user_TEST')
    # ### end Alembic commands ###
