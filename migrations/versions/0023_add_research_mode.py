"""empty message

Revision ID: 0023_add_research_mode
Revises: 0022_add_pending_status
Create Date: 2016-05-31 11:11:45.979594

"""

# revision identifiers, used by Alembic.
revision = '0023_add_research_mode'
down_revision = '0022_add_pending_status'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('services', sa.Column('research_mode', sa.Boolean(), nullable=True))
    op.add_column('services_history', sa.Column('research_mode', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('services_history', 'research_mode')
    op.drop_column('services', 'research_mode')
    ### end Alembic commands ###
