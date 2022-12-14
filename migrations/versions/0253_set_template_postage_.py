"""

Revision ID: 0253_set_template_postage
Revises: 0252_letter_branding_table
Create Date: 2019-01-30 16:47:08.599448

"""
from alembic import op
import sqlalchemy as sa


revision = '0253_set_template_postage'
down_revision = '0252_letter_branding_table'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(
        """UPDATE templates SET postage = services.postage
        FROM services WHERE template_type = 'letter' AND service_id = services.id"""
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("UPDATE templates SET postage = null WHERE template_type = 'letter'")
    # ### end Alembic commands ###