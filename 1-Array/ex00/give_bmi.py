def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """This function give the bmi at each element of
    the list using the formula weight / height **2
    and return a list of bmi"""
    bmi = [(a / b**2) for a, b in zip(weight, height)]
    return bmi


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """This function iterate at each element of the list
    , check if the element it's bigger than the limit
    and return a list of boolean"""
    limit = [a > limit for a in bmi]
    return limit
