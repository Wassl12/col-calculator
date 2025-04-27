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

new_york_tax_brackets = {
    0: 0.04,
    8501: 0.045,
    11701: 0.0525,
    13901: 0.059,
    21401: 0.0609,
    80651: 0.0641,
    215401: 0.0685,
    1077551: 0.0965,
    5000001: 0.103,
    25000001: 0.109
}

ny_standard_deduction = 8000

california_standard_deduction_2024 = 5540
california_state_personal_exemption_2024 = 149

class State(Enum):
    TEXAS = "texas"
    CALIFORNIA = "california"
    NEW_YORK = "new york"

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

NEW_YORK_RENT = {
    Quality.LOW: 2000,
    Quality.MEDIUM: 3000,
    Quality.HIGH: 4000,
    Quality.EXTREME: 4800
}


def calculate_state_income_tax(number: int, state: State, exemptions: int = 1) -> float:
    if state == State.TEXAS:
        return 0
    if state == State.CALIFORNIA:
        return calculate_progressive_tax(number - california_state_personal_exemption_2024 * exemptions, california_tax_brackets, california_standard_deduction_2024)
    if state == State.NEW_YORK:
        return calculate_progressive_tax(number - 0 * exemptions, new_york_tax_brackets, ny_standard_deduction) # idk the state p exemption

    
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
    if state == State.NEW_YORK:
        return (groceries + eat_out + gas + insurance + electricity + travel) * 1.3


    

def get_rent(quality: Quality, state: State):
    if state == State.TEXAS:
        return TEXAS_RENT[quality] * 12
    if state == State.CALIFORNIA:
        return CALIFORNIA_RENT[quality] * 12
    if state == State.NEW_YORK:
        return NEW_YORK_RENT[quality] * 12
    

