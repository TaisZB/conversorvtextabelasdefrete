import re
from decimal import Decimal

from core.detector import HeaderDetector
from core.mapper import ColumnMapper
from core.freight_table import FreightTable
from core.freight_row import FreightRow


class FreightConverter:

    def convert(self, sheet) -> FreightTable:
        table = FreightTable()

        header_row = HeaderDetector.detect(sheet)

        if header_row is None:
            raise Exception("Cabeçalho não encontrado.")

        if hasattr(sheet, "iloc"):
            headers = sheet.iloc[header_row - 1].tolist()
            rows = [sheet.iloc[index].tolist() for index in range(header_row, len(sheet.index))]
        else:
            headers = [cell.value for cell in sheet[header_row]]
            rows = [row for row in sheet.iter_rows(min_row=header_row + 1, values_only=True)]

        mapping = ColumnMapper.map_columns(headers)

        for row in rows:
            if mapping.zip_start is None or mapping.zip_end is None:
                continue

            if row[mapping.zip_start] is None:
                continue

            freight = FreightRow(
                zip_start=str(self._to_decimal(row[mapping.zip_start])),
                zip_end=str(self._to_decimal(row[mapping.zip_end])),
                weight_start=self._to_decimal(row[mapping.weight_start]) if mapping.weight_start is not None else Decimal("0"),
                weight_end=self._to_decimal(row[mapping.weight_end]) if mapping.weight_end is not None else Decimal("0"),
                delivery_time=self._to_int(row[mapping.delivery_time]) if mapping.delivery_time is not None else 0,
                price=self._to_decimal(row[mapping.price]) if mapping.price is not None else Decimal("0"),
                minimum_cost=self._to_decimal(row[mapping.minimum_cost]) if mapping.minimum_cost is not None else Decimal("0"),
                extra_weight=self._to_decimal(row[mapping.extra_weight]) if mapping.extra_weight is not None else Decimal("0"),
                price_percent=self._to_decimal(row[mapping.price_percent]) if mapping.price_percent is not None else Decimal("0"),
            )

            table.add(freight)

        return table

    @staticmethod
    def _to_decimal(value):
        if value is None:
            return Decimal("0")

        if hasattr(value, "item"):
            value = value.item()

        if isinstance(value, str):
            value = value.strip()
            if not value:
                return Decimal("0")
            value = value.replace(".", "", 1) if value.count(".") == 1 and value.replace(".", "", 1).isdigit() and value.count(",") == 0 else value
            value = value.replace(",", ".") if "," in value else value
            return Decimal(value)

        return Decimal(str(value))

    @staticmethod
    def _to_int(value):
        if value is None:
            return 0

        if hasattr(value, "item"):
            value = value.item()

        if isinstance(value, str):
            match = re.search(r"(\d+)", value)
            if match:
                return int(match.group(1))
            return 0

        return int(value)
