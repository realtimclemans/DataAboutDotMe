"""empty message

Revision ID: 26b35c87d834
Revises: b8347ee57d33
Create Date: 2020-12-29 01:12:23.342806

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26b35c87d834'
down_revision = 'b8347ee57d33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'dataset_metadata', ['table_name'])
    op.add_column('washington_state_voters', sa.Column('mail1', sa.String(), nullable=True))
    op.add_column('washington_state_voters', sa.Column('mail2', sa.String(), nullable=True))
    op.add_column('washington_state_voters', sa.Column('mail3', sa.String(), nullable=True))
    op.add_column('washington_state_voters', sa.Column('mail4', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'washington_state_voters', ['state_voter_id'])
    op.drop_column('washington_state_voters', 'mail')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('washington_state_voters', sa.Column('mail', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'washington_state_voters', type_='unique')
    op.drop_column('washington_state_voters', 'mail4')
    op.drop_column('washington_state_voters', 'mail3')
    op.drop_column('washington_state_voters', 'mail2')
    op.drop_column('washington_state_voters', 'mail1')
    op.drop_constraint(None, 'dataset_metadata', type_='unique')
    # ### end Alembic commands ###