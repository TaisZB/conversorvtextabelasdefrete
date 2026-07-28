"""
Mapeador inteligente de colunas.
"""

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class ColumnMap:
    zip_start: Optional[int] = None
    zip_end: Optional[int] = None
    weight_start: Optional[int] = None
    weight_end: Optional[int] = None
    delivery_time: Optional[int] = None
    price: Optional[int] = None
    minimum_cost: Optional[int] = None
    extra_weight: Optional[int] = None
    gris: Optional[int] = None
    toll: Optional[int] = None
    ad_valorem: Optional[int] = None
    price_percent: Optional[int] = None


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
        "weight_start": [
            "WEIGHTSTART",
            "PESO INICIAL",
            "PESO DE",
            "INITIAL WEIGHT"
        ],
        "weight_end": [
            "WEIGHTEND",
            "PESO FINAL",
            "PESO ATÉ",
            "FINAL WEIGHT"
        ],
        "delivery_time": [
            "PRAZO",
            "PRAZO(DIAS ÚTEIS)",
            "LEADTIME",
            "TIMECOST"
        ],
        "price": [
            "ABSOLUTEMONEYCOST",
            "VALOR",
            "FRETE",
            "PRICE"
        ],
        "minimum_cost": [
            "FRETE MÍNIMO",
            "FRETE MINIMO",
            "VALOR MÍNIMO",
            "MINIMUMVALUEINSURANCE"
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
        ],
        "price_percent": [
            "PRICEPERCENT",
            "% SOBRE NF",
            "PERCENTUAL"
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
