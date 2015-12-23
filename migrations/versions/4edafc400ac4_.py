"""empty message

Revision ID: 4edafc400ac4
Revises: None
Create Date: 2015-12-23 23:54:36.937417

"""

# revision identifiers, used by Alembic.
revision = '4edafc400ac4'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('email_address', sa.VARCHAR(length=30), nullable=False),
    sa.Column('active', sa.BOOLEAN(), server_default=sa.text(u'TRUE'), nullable=False),
    sa.Column('family_name', sa.VARCHAR(length=30), nullable=True),
    sa.Column('given_name', sa.VARCHAR(length=30), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email_address')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###
