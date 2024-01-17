from PIL import Image
import numpy as np

def ft_load(path: str) -> list:
    image = Image.open(path)
    im_matrix = np.array(image)
    print("The shape of image is:", im_matrix.shape)
    print(im_matrix)
    return im_matrix