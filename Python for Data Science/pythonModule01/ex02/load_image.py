from typing import Union
import numpy as np
from PIL import Image
import os

Array = Union[np.ndarray, list]

def ft_load(path: str) -> Array:
    """
    Load an image (JPG/JPEG), return its pixels as a numpy array.
    
    :param path: path to the image file
    :return: numpy array of shape (height, width, 3)
    :raises ValueError: if file does not exist or is not a JPG/JPEG
    """
    if not os.path.exists(path):
        raise ValueError(f"File not found: {path}")
    
    if not path.lower().endswith(('.jpg', '.jpeg')):
        raise ValueError("File must be JPG or JPEG format.")
    
    try:
        img = Image.open(path)
        img = img.convert("RGB")  # Ensure 3 channels
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
        print(img_array)
        return img_array
    except Exception as e:
        raise ValueError(f"Failed to load image: {e}")

def main():
    try:
        img_array = ft_load("landscape.jpg")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
