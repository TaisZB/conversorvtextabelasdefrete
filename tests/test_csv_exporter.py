from core.csv_exporter import CSVExporter


def test_csv_exporter():

    exporter = CSVExporter()

    rows = [
        {
            "CEP Inicial": "10000000",
            "CEP Final": "50000000",
            "Valor": "33.38"
        }
    ]

    exporter.export(rows, "frete_vtex.csv")

    assert True