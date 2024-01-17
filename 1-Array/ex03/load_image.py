from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """This function gonna load the image
    and return the the array of the image
    and print the shape of the image"""
    try:
        image = Image.open(path)
        im_matrix = np.array(image)
        print("The shape of image is:", im_matrix.shape)
        return im_matrix
    except FileNotFoundError or UnidentifiedImageError \
    or ValueError or TypeError as msg:
        print(msg)
        return