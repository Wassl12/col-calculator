from enum import Enum

from util.progressive_tax import calculate_progressive_tax

california_tax_brackets = {
    0: 0.01,
    10757: 0.02,
    25500: 0.04,
    40246: 0.06,
    55867: 0.08,
    70607: 0.093,
    360660: 0.103,
    432788: 0.113,
    721315: 0.123
}

california_standard_deduction_2024 = 5540
california_state_personal_exemption_2024 = 149

class State(Enum):
    TEXAS = "texas"
    CALIFORNIA = "california"

class Quality(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    EXTREME = "extreme"

CALIFORNIA_RENT = {
    Quality.LOW: 2000,
    Quality.MEDIUM: 2700,
    Quality.HIGH: 3300,
    Quality.EXTREME: 4000
}

TEXAS_RENT = {
    Quality.LOW: 900,
    Quality.MEDIUM: 1300,
    Quality.HIGH: 1600,
    Quality.EXTREME: 2000
}


def calculate_state_income_tax(number: int, state: State, exemptions: int = 1) -> float:
    if state == State.TEXAS:
        return 0
    if state == State.CALIFORNIA:
        return calculate_progressive_tax(number - california_state_personal_exemption_2024 * exemptions, california_tax_brackets, california_standard_deduction_2024)
    
def state_specific_expenses(quality: Quality, state: State):
    groceries = 3000
    eat_out = 3000
    gas = 300
    insurance = 2800
    electricity = 1800
    travel = 3000

    if state == State.TEXAS:
        return groceries + eat_out + gas + insurance + electricity + travel
    if state == State.CALIFORNIA:
        return (groceries + eat_out + gas + insurance + electricity + travel) * 1.15


    

def get_rent(quality: Quality, state: State):
    if state == State.TEXAS:
        return TEXAS_RENT[quality] * 12
    if state == State.CALIFORNIA:
        return CALIFORNIA_RENT[quality] * 12
    

