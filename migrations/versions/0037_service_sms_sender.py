"""empty message

Revision ID: 0037_service_sms_sender
Revises: 0036_notif_key_type_not_null
Create Date: 2016-06-30 14:55:33.811696

"""

# revision identifiers, used by Alembic.
revision = '0037_service_sms_sender'
down_revision = '0036_notif_key_type_not_null'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('services', sa.Column('sms_sender', sa.String(length=11), nullable=True))
    op.add_column('services_history', sa.Column('sms_sender', sa.String(length=11), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('services_history', 'sms_sender')
    op.drop_column('services', 'sms_sender')
    ### end Alembic commands ###
