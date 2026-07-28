from decimal import Decimal

from core.freight_table import FreightTable
from core.freight_row import FreightRow

table = FreightTable()

table.carrier = "Brunetto"

table.add(
    FreightRow(
        zip_start="90000000",
        zip_end="90099999",
        weight_start=Decimal("0"),
        weight_end=Decimal("10"),
        delivery_time=2,
        price=Decimal("18.50"),
        minimum_cost=Decimal("25"),
        extra_weight=Decimal("1.20")
    )
)

print(table.total_rows())
print(table.rows[0])
