from core.excel_reader import ExcelReader

reader = ExcelReader("input/SUA_PLANILHA.xlsx")

print(reader.get_sheet_names())
print(reader.get_dimensions())

for linha in reader.preview():
    print(linha)
