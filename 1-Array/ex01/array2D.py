import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """This function slice the y array of the family
       start at start a end one before the end,
       return the new array of sliced element"""
    try:
        assert isinstance(family, list) is True, "family is not a list"
        arr = np.array(family)
        print(f'My shape is : {arr.shape}')
        newarr = arr[start:end]
        print(f'My new shape is : {newarr.shape}')
        return newarr
    except AssertionError as msg:
        print("AssertionError:", msg)
