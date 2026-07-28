from decimal import Decimal

from core.excel_reader import ExcelReader
from core.converter import FreightConverter


def test_freight_rows_have_required_fields():
    reader = ExcelReader("input/freightModel.xls")

    sheet = reader.get_sheet()

    converter = FreightConverter()

    table = converter.convert(sheet)

    assert table.total_rows() == 6

    for row in table.rows:
        assert row.zip_start is not None
        assert row.zip_end is not None
        assert row.weight_start is not None
        assert row.weight_end is not None
        assert row.delivery_time is not None
        assert row.price is not None
        from decimal import Decimal


def test_first_freight_row_values():
    reader = ExcelReader("input/freightModel.xls")

    sheet = reader.get_sheet()

    converter = FreightConverter()

    table = converter.convert(sheet)

    row = table.rows[0]

    assert row.zip_start == "10000000"
    assert row.zip_end == "50000000"
    assert row.weight_start == Decimal("0")
    assert row.weight_end == Decimal("20")
    assert row.delivery_time == 3
    assert row.price == Decimal("33.38")
    assert row.extra_weight == Decimal("7.23")
    assert row.price_percent == Decimal("0.4")

