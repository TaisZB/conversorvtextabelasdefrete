from core.freight_converter import FreightConverter
from core.freight_calculator import FreightCalculator
from core.vtex_exporter import VtexExporter
from core.csv_exporter import CSVExporter

import pandas as pd


# arquivo de entrada
arquivo = "exemplo_frete.xlsx"

# lê planilha
sheet = pd.read_excel(arquivo)

# converte tabela
converter = FreightConverter()
freight_table = converter.convert(sheet)


# calcula valores VTEX
calculator = FreightCalculator()

rows = []

for row in freight_table.rows:
    price = calculator.calculate(row)

    rows.append({
        "CEP Inicial": row.zip_start,
        "CEP Final": row.zip_end,
        "Peso Inicial": row.weight_start,
        "Peso Final": row.weight_end,
        "Prazo": row.delivery_time,
        "Valor": price
    })


# gera arquivo VTEX
exporter = CSVExporter()

exporter.export(
    rows,
    "frete_vtex.csv"
)

print("Conversão concluída!")
print("Arquivo criado: frete_vtex.csv")
