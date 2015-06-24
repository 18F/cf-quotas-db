"""empty message

Revision ID: 354a51c6a9b
Revises: d869ae3c6
Create Date: 2015-05-28 12:52:03.035883

"""

# revision identifiers, used by Alembic.
revision = '354a51c6a9b'
down_revision = 'd869ae3c6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service', sa.Column('label', sa.String(), nullable=True))
    op.add_column('service', sa.Column('provider', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service', 'provider')
    op.drop_column('service', 'label')
    ### end Alembic commands ###
