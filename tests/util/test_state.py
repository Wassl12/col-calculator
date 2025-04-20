from util.state import State, calculate_state_income_tax


def test_state_basic():
    num = calculate_state_income_tax(5540, State.CALIFORNIA)
    assert num == 0

def test_state_basic_paying():
    num = calculate_state_income_tax(16000, State.CALIFORNIA)
    assert num == 103

def test_state_luke():
    num = calculate_state_income_tax(123_000, State.CALIFORNIA)
    assert num == 7452