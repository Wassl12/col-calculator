from util.federal import calculate_federal_income_tax

def test_federal_basic():
    num = calculate_federal_income_tax(10_000)
    assert num == 0

def test_federal_basic_paying():
    num = calculate_federal_income_tax(16_000)
    assert num == 140

def test_federal_luke():
    num = calculate_federal_income_tax(123_000)
    assert num == 19058