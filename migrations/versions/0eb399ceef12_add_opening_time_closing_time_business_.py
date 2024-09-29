"""Add opening_time, closing_time, business_days to User

Revision ID: 0eb399ceef12
Revises: 58168a60b622
Create Date: 2024-09-12 18:41:34.856621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0eb399ceef12'
down_revision = '58168a60b622'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('opening_time', sa.Time(), nullable=True))
        batch_op.add_column(sa.Column('closing_time', sa.Time(), nullable=True))
        batch_op.add_column(sa.Column('business_days', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('business_days')
        batch_op.drop_column('closing_time')
        batch_op.drop_column('opening_time')

    # ### end Alembic commands ###