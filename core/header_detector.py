"""
Detector inteligente de cabeçalhos de tabelas de frete.
"""

from typing import Optional, Any
from openpyxl.worksheet.worksheet import Worksheet


class HeaderDetector:

    KEYWORDS = [
        "CEPI",
        "CEP INICIAL",
        "CEP FINAL",
        "CEPF",
        "PRAZO",
        "PRAZO(DIAS ÚTEIS)",
        "FRETE",
        "FRETE MÍNIMO",
        "PESO",
        "VALOR",
        "GRIS",
        "PEDÁGIO",
        "AD VALOREM",
        "% SOBRE NF",
        "ZIPCODESTART",
        "ZIPCODEEND",
        "POLYGONNAME",
        "WEIGHTSTART",
        "WEIGHTEND",
        "ABSOLUTEMONEYCOST",
        "PRICEPERCENT",
        "PRICEBYEXTRAWEIGHT",
        "MAXVOLUME",
        "TIMECOST",
        "COUNTRY",
        "MINIMUMVALUEINSURANCE",
    ]

    @staticmethod
    def detect(sheet: Any, max_scan_rows: int = 30) -> Optional[int]:
        """
        Procura automaticamente a linha que contém o cabeçalho.

        Retorna o número da linha (1-based) ou None.
        """

        best_row = None
        best_score = 0

        if hasattr(sheet, "max_row"):
            max_row = min(sheet.max_row, max_scan_rows)
            rows = []
            for row in range(1, max_row + 1):
                values = []
                for cell in sheet[row]:
                    if cell.value is None:
                        continue
                    text = str(cell.value).strip().upper()
                    values.append(text)
                rows.append(values)
        else:
            max_row = min(len(sheet.index), max_scan_rows)
            rows = []
            for row in range(max_row):
                values = []
                for value in sheet.iloc[row].tolist():
                    if value is None:
                        continue
                    values.append(str(value).strip().upper())
                rows.append(values)

        for row_index, row_values in enumerate(rows, start=1):
            score = 0

            for keyword in HeaderDetector.KEYWORDS:
                if keyword in row_values:
                    score += 1

            if score > best_score:
                best_score = score
                best_row = row_index

        return best_row
