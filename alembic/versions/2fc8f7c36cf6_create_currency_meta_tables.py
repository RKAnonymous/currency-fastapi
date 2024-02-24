"""create currency, meta tables

Revision ID: 2fc8f7c36cf6
Revises: 
Create Date: 2024-02-23 13:53:51.140304

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "2fc8f7c36cf6"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def seeder():
    op.execute("INSERT INTO currency (id, base, last_update) VALUES (1, 'USD', NOW());")
    op.execute(
        """
        INSERT INTO meta (id, name, code, rate, currency_id)
        VALUES
        (1, 'Australian Dollar', 'AUD', 1.5237602167, 1),
        (2, 'Bulgarian Lev', 'BGN', 1.8007503552, 1),
        (3, 'Brazilian Real', 'BRL', 4.9929107983, 1),
        (4, 'Canadian Dollar', 'CAD', 1.3502001441, 1),
        (5, 'Swiss Franc', 'CHF', 0.8807401757, 1),
        (6, 'Chinese Yuan', 'CNY', 7.1941608798, 1),
        (7, 'Czech Republic Koruna', 'CZK', 23.4006134869, 1),
        (8, 'Danish Krone', 'DKK', 6.8876311314, 1),
        (9, 'Euro', 'EUR', 0.9238001386, 1),
        (10, 'British Pound Sterling', 'GBP', 0.7890401229, 1),
        (11, 'Hong Kong Dollar', 'HKD', 7.821451202, 1),
        (12, 'Croatian Kuna', 'HRK', 6.679631153, 1),
        (13, 'Hungarian Forint', 'HUF', 358.9667305737, 1),
        (14, 'Indonesian Rupiah', 'IDR', 15570.55921811, 1),
        (15, 'Israeli New Sheqel', 'ILS', 3.6240804528, 1),
        (16, 'Indian Rupee', 'INR', 82.8202035907, 1),
        (17, 'Icelandic Króna', 'ISK', 136.9745258003, 1),
        (18, 'Japanese Yen', 'JPY', 150.4576639097, 1),
        (19, 'South Korean Won', 'KRW', 1328.3914832597, 1),
        (20, 'Mexican Peso', 'MXN', 17.1175521075, 1),
        (21, 'Malaysian Ringgit', 'MYR', 4.7746505677, 1),
        (22, 'Norwegian Krone', 'NOK', 10.5387614626, 1),
        (23, 'New Zealand Dollar', 'NZD', 1.6134502847, 1),
        (24, 'Philippine Peso', 'PHP', 55.886418734, 1),
        (25, 'Polish Zloty', 'PLN', 3.9763004773, 1),
        (26, 'Romanian Leu', 'RON', 4.5955506449, 1),
        (27, 'Russian Ruble', 'RUB', 94.7394773803, 1),
        (28, 'Swedish Krona', 'SEK', 10.3160119867, 1),
        (29, 'Singapore Dollar', 'SGD', 1.3418801356, 1),
        (30, 'Thai Baht', 'THB', 35.9058263703, 1),
        (31, 'Turkish Lira', 'TRY', 30.966103637, 1),
        (32, 'US Dollar', 'USD', 1, 1),
        (33, 'South African Rand', 'ZAR', 19.2908925499, 1);
        """
    )


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "currency",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("base", sa.String(), nullable=False),
        sa.Column("last_update", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_currency_base"), "currency", ["base"], unique=False)
    op.create_table(
        "meta",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("currency_id", sa.Integer(), nullable=True),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("code", sa.String(), nullable=False),
        sa.Column("rate", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(["currency_id"], ["currency.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_meta_code"), "meta", ["code"], unique=False)
    # ### end Alembic commands ###

    seeder()  # Insert predefined data


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_meta_code"), table_name="meta")
    op.drop_table("meta")
    op.drop_index(op.f("ix_currency_base"), table_name="currency")
    op.drop_table("currency")
    # ### end Alembic commands ###
