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
        