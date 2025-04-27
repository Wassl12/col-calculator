"""Services for computing taxes."""
from util.federal import calculate_federal_income_tax, calculate_fica
from util.local import City, calculate_local_income_tax
from util.state import State, calculate_state_income_tax


def get_all_taxes(salary: int, state: str, exemptions: int, city: City = City.OTHER):
    "Get all your major taxes for a given state and city. If no city is provided, assume there is no city income tax."
    return round(calculate_federal_income_tax(salary) + calculate_state_income_tax(salary, State(state.lower()), exemptions) + calculate_fica(salary) + calculate_local_income_tax(salary, city))
