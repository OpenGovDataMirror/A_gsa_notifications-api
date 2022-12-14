"""empty message

Revision ID: 0029_fix_email_from
Revises: 0028_fix_reg_template_history
Create Date: 2016-06-13 15:15:34.035984

"""

# revision identifiers, used by Alembic.
revision = '0029_fix_email_from'
down_revision = '0028_fix_reg_template_history'

from alembic import op
import sqlalchemy as sa

service_id = 'd6aa2c68-a2d9-4437-ab19-3ae8eb202553'
def upgrade():
    op.get_bind()
    op.execute("update services set email_from = 'testsender' where id = '{}'".format(service_id))
    op.execute("update services_history set email_from = 'testsender' where id = '{}'".format(service_id))


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###