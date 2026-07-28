from core.excel_reader import ExcelReader
from core.detector import HeaderDetector
from core.mapper import ColumnMapper

reader = ExcelReader("input/freightModel.xls")

sheet = reader.get_sheet()
header = HeaderDetector.detect(sheet)

if hasattr(sheet, "iloc"):
    cells = sheet.iloc[header - 1].tolist()
else:
    cells = [c.value for c in sheet[header]]

mapping = ColumnMapper.map_columns(cells)

print(mapping)
