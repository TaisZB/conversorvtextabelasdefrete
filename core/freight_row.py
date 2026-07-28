from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass
class FreightRow:
    """
    Modelo interno universal de uma linha de frete.
    Todas as transportadoras serão convertidas para este formato.
    """

    zip_start: str
    zip_end: str

    weight_start: Decimal
    weight_end: Decimal

    delivery_time: int

    price: Decimal

    minimum_cost: Decimal = Decimal("0")

    extra_weight: Decimal = Decimal("0")

    gris: Decimal = Decimal("0")

    toll: Decimal = Decimal("0")

    ad_valorem: Decimal = Decimal("0")

    price_percent: Decimal = Decimal("0")

    dispatch_cost: Decimal = Decimal("0")

    interior_additional: Decimal = Decimal("0")

    notes: Optional[str] = None
