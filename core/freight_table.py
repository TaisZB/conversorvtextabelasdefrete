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