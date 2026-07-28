from dataclasses import dataclass, field
from typing import List

from .freight_row import FreightRow


@dataclass
class FreightTable:

    carrier: str = ""

    source_file: str = ""

    rows: List[FreightRow] = field(default_factory=list)

    def add(self, row: FreightRow):
        self.rows.append(row)

    def total_rows(self):
        return len(self.rows)

    def is_empty(self):
        return len(self.rows) == 0
from dataclasses import dataclass, field
from typing import List, Optional
from decimal import Decimal

from .freight_row import FreightRow


@dataclass
class FreightTable:

    carrier: str = ""

    source_file: str = ""

    rows: List[FreightRow] = field(default_factory=list)

    def add(self, row: FreightRow):
        self.rows.append(row)

    def total_rows(self):
        return len(self.rows)

    def is_empty(self):
        return len(self.rows) == 0

    def find(self, zipcode: str, weight: Decimal) -> Optional[FreightRow]:
        zipcode = zipcode.replace("-", "")

        for row in self.rows:
            if (
                row.zip_start <= zipcode <= row.zip_end
                and row.weight_start <= weight <= row.weight_end
            ):
                return row

        return None
        from decimal import Decimal

from core.excel_reader import ExcelReader
from core.converter import FreightConverter


def test_find_freight_by_zip_and_weight():

    reader = ExcelReader("input/freightModel.xls")

    sheet = reader.get_sheet()

    converter = FreightConverter()

    table = converter.convert(sheet)

    row = table.find(
        "15000000",
        Decimal("10")
    )

    assert row is not None
    assert row.price == Decimal("33.38")
    assert row.delivery_time == 3
    