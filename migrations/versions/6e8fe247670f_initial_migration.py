"""initial migration

Revision ID: 6e8fe247670f
Revises: 
Create Date: 2025-05-04 13:16:09.040092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e8fe247670f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('photo', sa.String(length=255), nullable=False),
    sa.Column('date_joined', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('favourites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_fk', sa.Integer(), nullable=False),
    sa.Column('fav_user_id_fk', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['fav_user_id_fk'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id_fk'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id_fk', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('parish', sa.String(length=100), nullable=True),
    sa.Column('biography', sa.Text(), nullable=True),
    sa.Column('sex', sa.String(length=20), nullable=True),
    sa.Column('race', sa.String(length=50), nullable=True),
    sa.Column('birth_year', sa.Integer(), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('fav_cuisine', sa.String(length=100), nullable=True),
    sa.Column('fav_colour', sa.String(length=50), nullable=True),
    sa.Column('fav_school_subject', sa.String(length=100), nullable=True),
    sa.Column('political', sa.Boolean(), nullable=True),
    sa.Column('religious', sa.Boolean(), nullable=True),
    sa.Column('family_oriented', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id_fk'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    op.drop_table('favourites')
    op.drop_table('users')
    # ### end Alembic commands ###
