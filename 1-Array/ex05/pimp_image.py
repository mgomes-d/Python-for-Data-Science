import numpy as np
from PIL import Image


# def ft_invert(array) -> array:
#     #your code here

# def ft_red(array) -> array:
#     #ref

def ft_green(array) -> np.ndarray:

    newarray = [z for z in array]

    # Convertir le tableau NumPy modifié en image
    modified_image = Image.fromarray(newarray)

    # Afficher les images
    modified_image.show()
    return array

# def ft_blue(array) -> array:
#     #your code here

# def ft_grey(array) -> array:
#     #your code here
