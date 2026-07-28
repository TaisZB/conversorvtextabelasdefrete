from core.excel_reader import ExcelReader
from core.converter import FreightConverter

reader = ExcelReader("input/freightModel.xls")

sheet = reader.get_sheet()

converter = FreightConverter()

table = converter.convert(sheet)

print(table.total_rows())
print(table.rows[0])
