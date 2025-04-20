from util.federal import calculate_federal_income_tax, calculate_fica
from util.state import State, calculate_state_income_tax

def get_all_taxes(salary: int, state: str, exemptions: int):
    return round(calculate_federal_income_tax(salary) + calculate_state_income_tax(salary, State(state.lower()), exemptions) + calculate_fica(salary))