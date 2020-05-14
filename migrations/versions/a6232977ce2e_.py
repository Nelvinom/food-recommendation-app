"""empty message

Revision ID: a6232977ce2e
Revises: 
Create Date: 2020-05-14 16:31:18.662721

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6232977ce2e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('foods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_foods_name'), 'foods', ['name'], unique=True)
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_path', sa.String(), nullable=True),
    sa.Column('food_review', sa.String(), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('food_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['food_id'], ['foods.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('restaurants', sa.Column('food_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'restaurants', 'foods', ['food_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'restaurants', type_='foreignkey')
    op.drop_column('restaurants', 'food_id')
    op.drop_table('reviews')
    op.drop_index(op.f('ix_foods_name'), table_name='foods')
    op.drop_table('foods')
    # ### end Alembic commands ###
