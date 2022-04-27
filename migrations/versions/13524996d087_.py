"""empty message

Revision ID: 13524996d087
Revises: 4e5563237403
Create Date: 2022-04-26 21:36:56.721540

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '13524996d087'
down_revision = '4e5563237403'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('classroom', sa.VARCHAR(length=50), nullable=True))
    op.add_column('course', sa.Column('teacher', sa.VARCHAR(length=50), nullable=True))
    op.add_column('course', sa.Column('course_color', sa.VARCHAR(length=50), nullable=True))
    op.add_column('course', sa.Column('x', sa.Integer(), nullable=True))
    op.add_column('course', sa.Column('y', sa.Integer(), nullable=True))
    op.add_column('course', sa.Column('front_id', sa.Integer(), nullable=True))
    op.add_column('course', sa.Column('user_email', sa.VARCHAR(length=50), nullable=True))
    op.alter_column('course', 'course_name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=True)
    op.drop_column('course', 'Room')
    op.drop_column('course', 'From')
    op.drop_column('course', 'Lecturer')
    op.drop_column('course', 'To')
    op.drop_column('course', 'color')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('course', sa.Column('color', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('course', sa.Column('To', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('course', sa.Column('Lecturer', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('course', sa.Column('From', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('course', sa.Column('Room', mysql.VARCHAR(length=50), nullable=False))
    op.alter_column('course', 'course_name',
               existing_type=mysql.VARCHAR(length=50),
               nullable=False)
    op.drop_column('course', 'user_email')
    op.drop_column('course', 'front_id')
    op.drop_column('course', 'y')
    op.drop_column('course', 'x')
    op.drop_column('course', 'course_color')
    op.drop_column('course', 'teacher')
    op.drop_column('course', 'classroom')
    # ### end Alembic commands ###