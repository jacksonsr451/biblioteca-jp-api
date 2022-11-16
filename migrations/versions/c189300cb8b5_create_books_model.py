"""Create books model

Revision ID: c189300cb8b5
Revises:
Create Date: 2022-11-16 11:40:17.653037
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'c189300cb8b5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'books',
        sa.Column('isbn', sa.String(length=36), nullable=False),
        sa.Column('book_name', sa.String(length=100), nullable=False),
        sa.Column('author', sa.String(length=100), nullable=False),
        sa.Column('co_author', sa.String(length=255), nullable=True),
        sa.Column('publishing_company', sa.String(length=100), nullable=False),
        sa.Column('area', sa.String(length=50), nullable=False),
        sa.Column('shelf', sa.String(length=50), nullable=False),
        sa.Column('included_at', sa.String(length=9), nullable=True),
        sa.Column('updated_at', sa.String(length=9), nullable=True),
        sa.PrimaryKeyConstraint('isbn'),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    # ### end Alembic commands ###
