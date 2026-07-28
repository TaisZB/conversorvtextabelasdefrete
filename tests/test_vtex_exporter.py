from decimal import Decimal

from core.vtex_exporter import VtexExporter
from core.freight_table import FreightTable
from core.freight_row import FreightRow


def test_export_vtex():

    table = FreightTable()

    table.add(
        FreightRow(
            zip_start="10000000",
            zip_end="50000000",
            weight_start=Decimal("0"),
            weight_end=Decimal("20"),
            delivery_time=3,
            price=Decimal("33.38"),
        )
    )

    exporter = VtexExporter()

    result = exporter.export(table)

    assert len(result) == 1

    assert result[0]["cepInicial"] == "10000000"
    assert result[0]["cepFinal"] == "50000000"
    assert result[0]["prazo"] == 3
    