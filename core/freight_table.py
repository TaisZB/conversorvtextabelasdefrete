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
