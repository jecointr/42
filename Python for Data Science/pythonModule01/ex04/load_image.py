# load_image.py
from typing import Union
import numpy as np
from PIL import Image
import os

Array = Union[np.ndarray, list]

def ft_load(path: str) -> np.ndarray:
    """
    Load an image (JPG/JPEG) and return its pixels as a numpy array.
    
    :param path: path to the image file
    :return: numpy array of shape (height, width, 3)
    :raises ValueError: if file does not exist or is not JPG/JPEG
    """
    if not os.path.exists(path):
        raise ValueError(f"File not found: {path}")
    
    if not path.lower().endswith(('.jpg', '.jpeg')):
        raise ValueError("File must be JPG or JPEG format.")
    
    try:
        img = Image.open(path).convert("RGB")  # ensure 3 channels
        img_array = np.array(img)
        return img_array
    except Exception as e:
        raise ValueError(f"Failed to load image: {e}")

# Optional main for local testing
def main():
    try:
        img_array = ft_load("animal.jpeg")
        print(f"The shape of image is: {img_array.shape}")
        print(img_array)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

