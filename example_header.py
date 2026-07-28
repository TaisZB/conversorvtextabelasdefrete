from core.excel_reader import ExcelReader
from core.detector import HeaderDetector

reader = ExcelReader("input/freightModel.xls")

sheet = reader.get_sheet()
header = HeaderDetector.detect(sheet)

print("Cabeçalho encontrado:", header)
