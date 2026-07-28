import os
import unittest
from decimal import Decimal

from core.excel_reader import ExcelReader
from core.freight_converter import FreightConverter


class FreightConverterTest(unittest.TestCase):

    def test_convert_sample_workbook(self):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        workbook_path = os.path.join(base_dir, "input", "freightModel.xls")

        reader = ExcelReader(workbook_path)
        sheet = reader.get_sheet()

        converter = FreightConverter()
        table = converter.convert(sheet)

        self.assertEqual(table.total_rows(), 6)

        first_row = table.rows[0]
        self.assertEqual(first_row.zip_start, "10000000")
        self.assertEqual(first_row.zip_end, "50000000")
        self.assertEqual(first_row.weight_start, Decimal("0"))
        self.assertEqual(first_row.weight_end, Decimal("20"))
        self.assertEqual(first_row.delivery_time, 3)
        self.assertEqual(first_row.price, Decimal("33.38"))
        self.assertEqual(first_row.price_percent, Decimal("0.4"))
        self.assertEqual(first_row.extra_weight, Decimal("7.23"))


if __name__ == "__main__":
    unittest.main()
