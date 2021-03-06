"""empty message

Revision ID: 056e87a14b2e
Revises: 
Create Date: 2021-03-02 22:05:39.531508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '056e87a14b2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('personaje',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('height', sa.String(length=100), nullable=False),
    sa.Column('gender', sa.String(length=200), nullable=False),
    sa.Column('hair_color', sa.String(length=200), nullable=False),
    sa.Column('eye_color', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('planetas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=True),
    sa.Column('diameter', sa.String(length=300), nullable=False),
    sa.Column('rotation_period', sa.String(length=300), nullable=False),
    sa.Column('gravity', sa.String(length=300), nullable=False),
    sa.Column('population', sa.String(length=300), nullable=False),
    sa.Column('climate', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('gender', sa.String(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favoritos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('personajes_name', sa.String(length=250), nullable=True),
    sa.Column('planetas_name', sa.String(length=250), nullable=True),
    sa.Column('user_name', sa.String(length=250), nullable=True),
    sa.ForeignKeyConstraint(['personajes_name'], ['personaje.name'], ),
    sa.ForeignKeyConstraint(['planetas_name'], ['planetas.name'], ),
    sa.ForeignKeyConstraint(['user_name'], ['user.name'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favoritos')
    op.drop_table('user')
    op.drop_table('planetas')
    op.drop_table('personaje')
    # ### end Alembic commands ###
