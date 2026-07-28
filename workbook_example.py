from core.excel_reader import ExcelReader
from core.freight_converter import FreightConverter

reader = ExcelReader("input/freightModel.xls")
sheet = reader.get_sheet()
converter = FreightConverter()
table = converter.convert(sheet)

print(f"Linhas convertidas: {table.total_rows()}")
for row in table.rows[:3]:
    print(row)
