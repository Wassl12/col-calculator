from util.progressive_tax import calculate_progressive_tax


BRACKETS_2025 = {
    0: 0.10,
    11925: 0.12,
    48475: 0.22,
    103350: 0.24,
    197300: 0.32,
    250525: 0.35,
    626350: 0.37,
}

BRACKETS_2024 = {
    0: 0.10,
    11600: 0.12,
    47150: 0.22,
    100525: 0.24,
    191950: 0.32,
    243725: 0.35,
    609350: 0.37,
}

STANDARD_DEDUCTION_2025 = 15000

STANDARD_DEDUCTION_2024 = 14600


def calculate_federal_income_tax(number: int) -> float:
    return calculate_progressive_tax(number, BRACKETS_2024, STANDARD_DEDUCTION_2024)


def calculate_fica(number: int) -> float:
    return number * 0.0765
