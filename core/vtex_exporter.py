from decimal import Decimal

from core.freight_table import FreightTable
from core.freight_calculator import FreightCalculator


class VtexExporter:

    def __init__(self):
        self.calculator = FreightCalculator()

    def export(self, table: FreightTable):

        result = []

        for row in table.rows:
            value = self.calculator.calculate(row)

            result.append(
                {
                    "cepInicial": row.zip_start,
                    "cepFinal": row.zip_end,
                    "pesoInicial": str(row.weight_start),
                    "pesoFinal": str(row.weight_end),
                    "prazo": row.delivery_time,
                    "valor": str(value),
                }
            )

        return result