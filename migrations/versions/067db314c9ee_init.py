"""init

Revision ID: 067db314c9ee
Revises: 
Create Date: 2017-12-11 22:27:31.511972

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '067db314c9ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('campaign',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('contact_email', sa.Unicode(length=254), nullable=False),
    sa.Column('name', sa.Unicode(length=250), nullable=False),
    sa.Column('title', sa.Unicode(length=250), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('subscriber',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('email', sa.Unicode(length=254), nullable=False),
    sa.Column('first_name', sa.Unicode(length=255), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('auto_responder',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('campaign_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('subject', sa.Unicode(length=255), nullable=False),
    sa.Column('frequency', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaign.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('incoming_message',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('from_address', sa.Unicode(length=254), nullable=False),
    sa.Column('to_address', sa.Unicode(length=254), nullable=False),
    sa.Column('subject', sa.Unicode(length=255), nullable=False),
    sa.Column('headers', sa.UnicodeText(), nullable=False),
    sa.Column('messageid', sa.Unicode(length=255), nullable=False),
    sa.Column('body', sa.UnicodeText(), nullable=True),
    sa.Column('campaign_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaign.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('outgoing_message',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('to_addresses', postgresql.ARRAY(sa.Unicode(), dimensions=1), nullable=False),
    sa.Column('cc_list', postgresql.ARRAY(sa.Unicode(), dimensions=1), nullable=True),
    sa.Column('bcc_list', postgresql.ARRAY(sa.Unicode(), dimensions=1), nullable=True),
    sa.Column('subject', sa.Unicode(length=255), nullable=False),
    sa.Column('headers', sa.UnicodeText(), nullable=True),
    sa.Column('messageid', sa.Unicode(length=255), nullable=False),
    sa.Column('campaign_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaign.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subscription',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('token', sa.Unicode(length=22), nullable=False),
    sa.Column('campaign_id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('subscriber_id', sa.Integer(), nullable=False),
    sa.Column('active', sa.Boolean(), nullable=False),
    sa.Column('unsubscribed_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaign.id'], ),
    sa.ForeignKeyConstraint(['subscriber_id'], ['subscriber.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('response_template',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('auto_responder_id', sa.Integer(), nullable=False),
    sa.Column('lang_code', sa.Unicode(length=3), nullable=False),
    sa.Column('body', sa.UnicodeText(), nullable=True),
    sa.Column('name', sa.Unicode(length=250), nullable=False),
    sa.Column('title', sa.Unicode(length=250), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['auto_responder_id'], ['auto_responder.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )


def downgrade():
    op.drop_table('response_template')
    op.drop_table('subscription')
    op.drop_table('outgoing_message')
    op.drop_table('incoming_message')
    op.drop_table('auto_responder')
    op.drop_table('subscriber')
    op.drop_table('campaign')
