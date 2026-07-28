"""
Mapeador inteligente de colunas.
"""

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class ColumnMap:
    zip_start: Optional[int] = None
    zip_end: Optional[int] = None
    delivery_time: Optional[int] = None
    minimum_cost: Optional[int] = None
    extra_weight: Optional[int] = None
    gris: Optional[int] = None
    toll: Optional[int] = None
    ad_valorem: Optional[int] = None


class ColumnMapper:

    SYNONYMS: Dict[str, list[str]] = {
        "zip_start": [
            "CEPI",
            "CEP INICIAL",
            "CEP ORIGEM",
            "ZIPCODESTART",
            "ZIP START"
        ],
        "zip_end": [
            "CEPF",
            "CEP FINAL",
            "CEP DESTINO",
            "ZIPCODEEND",
            "ZIP END"
        ],
        "delivery_time": [
            "PRAZO",
            "PRAZO(DIAS ÚTEIS)",
            "LEADTIME"
        ],
        "minimum_cost": [
            "FRETE MÍNIMO",
            "FRETE MINIMO",
            "VALOR MÍNIMO"
        ],
        "extra_weight": [
            "VALOR POR KG",
            "EXCESSO",
            "PRICEBYEXTRAWEIGHT"
        ],
        "gris": [
            "GRIS"
        ],
        "toll": [
            "PEDÁGIO",
            "PEDAGIO"
        ],
        "ad_valorem": [
            "AD VALOREM",
            "% SOBRE NF"
        ]
    }

    @staticmethod
    def map_columns(header_row) -> ColumnMap:

        mapping = ColumnMap()

        for index, cell in enumerate(header_row):
            if cell is None:
                continue

            value = str(cell).strip().upper()

            for attribute, aliases in ColumnMapper.SYNONYMS.items():
                if value in aliases:
                    setattr(mapping, attribute, index)

        return mapping
