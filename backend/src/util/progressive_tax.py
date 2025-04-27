def calculate_progressive_tax(
    number: float, lower_brackets: dict[int, float], deduction: float
):
    number = max(number - deduction, 0)
    upper_brackets = create_upper_bounds(lower_brackets)
    total = 0
    prior_amount = 0
    for amount, rate in upper_brackets.items():
        total += min(amount - prior_amount, number) * rate
        number -= min(amount - prior_amount, number)
        if number == 0:
            break
        prior_amount = amount
    return int(total)


def create_upper_bounds(brackets: dict[int, float]):
    upper_brackets = {}
    prior_amount, prior_rate = None, None
    for amount, rate in brackets.items():
        if prior_amount is not None:
            upper_brackets[amount] = prior_rate
        prior_amount = amount
        prior_rate = rate
    upper_brackets[float("inf")] = prior_rate
    return upper_brackets
