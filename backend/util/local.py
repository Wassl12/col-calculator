from util.progressive_tax import calculate_progressive_tax
from enum import Enum

nyc_tax_brackets = {
    0: 0.03078,
    12000: 0.03762,
    25000: 0.03819,
    50000: 0.03876
}

class City(Enum):
    NYC = "nyc"
    OTHER = "other"


def calculate_local_income_tax(number: int, city: City):
    if city != City.NYC:
        return 0
    return calculate_progressive_tax(number, nyc_tax_brackets, 8000)