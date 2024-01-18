import numpy as np
from PIL import Image


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    img_arr = array.copy()
    red_channel = img_arr[:, :, 0]
    green_channel = img_arr[:, :, 1]
    blue_channel = img_arr[:, :, 2]
    img_arr[:, :, 0] = 255 - red_channel
    img_arr[:, :, 1] = 255 - green_channel
    img_arr[:, :, 2] = 255 - blue_channel
    img = Image.fromarray(img_arr)
    img.show()
    return array


def ft_red(array) -> np.ndarray:
    """Change the color filter to red."""
    img_arr = array.copy()
    img_arr[:, :, 1] = 0
    img_arr[:, :, 2] = 0

    img = Image.fromarray(img_arr)
    img.show()
    return array


def ft_green(array) -> np.ndarray:
    """Change the color filter to green."""
    img_arr = array.copy()
    img_arr[:, :, 0] = 0
    img_arr[:, :, 2] = 0

    img = Image.fromarray(img_arr)
    img.show()
    return array


def ft_blue(array) -> np.ndarray:
    """Change the color filter to blue."""
    img_arr = array.copy()
    img_arr[:, :, 0] = 0
    img_arr[:, :, 1] = 0

    img = Image.fromarray(img_arr)
    img.show()
    return array


def ft_grey(array) -> np.ndarray:
    """Change the color filter to grey."""
    img_arr = array.copy()
    red_channel = img_arr[:, :, 0] / 3
    green_channel = img_arr[:, :, 1] / 3
    blue_channel = img_arr[:, :, 2] / 3
    grey_channel = red_channel + green_channel + blue_channel
    img_arr[:, :, 0] = grey_channel
    img_arr[:, :, 1] = grey_channel
    img_arr[:, :, 2] = grey_channel

    img = Image.fromarray(img_arr)
    img.show()
    return array
