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


def test_calculate_extra_weight():

    row = FreightRow(
        zip_start="10000000",
        zip_end="50000000",
        weight_start=Decimal("0"),
        weight_end=Decimal("20"),
        delivery_time=3,
        price=Decimal("33.38"),
        extra_weight=Decimal("7.23")
    )

    calculator = FreightCalculator()

    valor = calculator.calculate(row, weight=Decimal("25"))

def test_calculate_extra_weight():

    row = FreightRow(
        zip_start="10000000",
        zip_end="50000000",
        weight_start=Decimal("0"),
        weight_end=Decimal("20"),
        delivery_time=3,
        price=Decimal("33.38"),
        extra_weight=Decimal("7.23")
    )

    calculator = FreightCalculator()

    valor = calculator.calculate(row, weight=Decimal("25"))

    assert valor > Decimal("33.38")
