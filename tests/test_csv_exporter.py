from core.csv_exporter import CsvExporter


def test_export_csv(tmp_path):

    data = [
        {
            "cepInicial": "10000000",
            "cepFinal": "50000000",
            "pesoInicial": "0",
            "pesoFinal": "20",
            "prazo": 3,
            "valor": "33.51352",
        }
    ]

    file = tmp_path / "frete.csv"

    exporter = CsvExporter()

    exporter.export(data, file)

    content = file.read_text(encoding="utf-8")

    assert "cepInicial" in content
    assert "10000000" in content
    assert "33.51352" in content