from load_image import ft_load
import numpy as np
from PIL import Image


def slice_me(family: np.ndarray, start: int, end: int) -> np.ndarray:
    """This function slice the y array of the family
       start at start a end one before the end,
       return the new array of sliced element"""
    try:
        assert isinstance(family, np.ndarray) is True, "family is not a np.ndarray"
        arr = np.array(family)
        print(f'My shape is : {arr.shape}')
        newarr = arr[start:end, start:end, 2]
        print(f'My new shape is : {newarr.shape}')
        return newarr
    except AssertionError as msg:
        print("AssertionError:", msg)
        return


def main():
    img_array = ft_load("animal.jpeg")
    if img_array is None:
        return 1
    print(img_array)
    new_img_array = slice_me(img_array, 350, 750)
    if new_img_array is None:
        return 1
    new_img = Image.fromarray(new_img_array)
    new_img.show()


if __name__ == "__main__":
    main()
