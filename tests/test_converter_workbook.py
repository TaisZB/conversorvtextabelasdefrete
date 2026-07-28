from core.excel_reader import ExcelReader
from core.converter import FreightConverter


def test_workbook_conversion_creates_rows():
    reader = ExcelReader("input/freightModel.xls")

    sheet = reader.get_sheet()

    converter = FreightConverter()

    table = converter.convert(sheet)

    assert table.total_rows() == 6
    assert table.rows[0] is not None