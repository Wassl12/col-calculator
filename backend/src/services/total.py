"""Service file for computing the total cost of living somewhere."""

from services.taxes import get_all_taxes
from util.local import City
from util.state import Quality, State, get_rent, state_specific_expenses


def get_total(
    salary: int, state: str, exemptions: int, quality: str, k: int, city: City
):
    """Get the total cost for living in a state given the parameters."""
    state = state.lower()
    after_401k = salary - k
    after_taxes = after_401k - get_all_taxes(after_401k, state, exemptions, city)

    total = after_taxes - get_rent(Quality(quality), State(state)) + k

    total -= state_specific_expenses(Quality(quality), State(state))
    return total
