from decimal import Decimal

from core.freight_row import FreightRow


class FreightCalculator:

    def calculate(self, row: FreightRow) -> Decimal:

        price = row.price

        if row.price_percent > 0:
            price += price * (row.price_percent / Decimal("100"))

        if row.minimum_cost > price:
            price = row.minimum_cost

        return price
        from decimal import Decimal

from core.freight_calculator import FreightCalculator
from core.freight_row import FreightRow


def test_calculate_freight_price():

    row = FreightRow(
        zip_start="10000000",
        zip_end="50000000",
        weight_start=Decimal("0"),
        weight_end=Decimal("20"),
        delivery_time=3,
        price=Decimal("33.38"),
        price_percent=Decimal("0.4")
    )

    calculator = FreightCalculator()

    result = calculator.calculate(row)

    assert result == Decimal("33.51352")
    valor = calculator.calculate(row, weight=Decimal("25"))
from decimal import Decimal

from core.freight_row import FreightRow


class FreightCalculator:

    def calculate(self, row: FreightRow, weight=None):
        price = row.price

        if row.price_percent:
            price += price * row.price_percent / Decimal("100")

        if weight and weight > row.weight_end:
            excess = weight - row.weight_end
            price += excess * row.extra_weight

        if price < row.minimum_cost:
            price = row.minimum_cost

        return price
