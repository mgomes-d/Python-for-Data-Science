from load_image import ft_load
import numpy as np
from PIL import Image


def slice_me(family: np.ndarray, start: int, end: int) -> np.ndarray:
    """This function slice the y array of the family
       start at start a end one before the end,
       return the new array of sliced element"""
    try:
        assert isinstance(family, np.ndarray) is True, \
            "family is not a np.ndarray"
        arr = np.array(family)
        newarr = arr[start:end, start:end, 1]
        return newarr
    except AssertionError as msg:
        print("AssertionError:", msg)
        return


def main():
    img_array = ft_load("animal.jpeg")
    if img_array is None:
        return 1
    new_img_array = slice_me(img_array, 350, 750)
    if new_img_array is None:
        return 1
    print("The shape of the image is:", new_img_array.shape)
    print(new_img_array)
    img_array_transpose = new_img_array.T
    print("New shape after Transpose:", img_array_transpose.shape)
    print(img_array_transpose)
    new_img = Image.fromarray(img_array_transpose)
    new_img.show()


if __name__ == "__main__":
    main()
