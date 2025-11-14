# zoom.py
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(img_array: np.ndarray, x_start: int, y_start: int,
               width: int, height: int) -> np.ndarray:
    """
    Crop a portion of the image (zoom) and convert to single channel (red).

    :param img_array: numpy array of the image (H, W, 3)
    :param x_start: starting x coordinate
    :param y_start: starting y coordinate
    :param width: width of the zoom area
    :param height: height of the zoom area
    :return: cropped image array (single channel)
    """
    H, W, C = img_array.shape
    if C != 3:
        raise ValueError("Input image must have 3 channels (RGB)")

    if x_start < 0 or y_start < 0 or x_start + width > W \
       or y_start + height > H:
        raise ValueError("Zoom area is out of image bounds")

    cropped = img_array[y_start:y_start + height, x_start:x_start + width, :]
    # Extraire le canal rouge pour simuler l'exemple
    red_channel = cropped[:, :, 0][:, :, np.newaxis]

    # print avec exactement la phrase du sujet
    print(
        f"New shape after slicing: {red_channel.shape} or "
        f"({red_channel.shape[0]}, {red_channel.shape[1]})"
    )
    print(red_channel)

    return red_channel


def display_image(img_array: np.ndarray, title="Zoomed Image"):
    """Display a single-channel image with matplotlib."""
    plt.imshow(img_array[:, :, 0], cmap='gray')
    plt.title(title)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()


def main():
    try:
        # Charger l'image
        img_array = ft_load("animal.jpeg")
        print(f"The shape of image is: {img_array.shape}")
        print(img_array)

        # Zoom centré sur un carré de 400x400
        zoom_size = 400
        H, W, _ = img_array.shape
        x_start = max((W - zoom_size) // 2, 0)
        y_start = max((H - zoom_size) // 2, 0)

        zoomed_img = zoom_image(img_array, x_start, y_start,
                                zoom_size, zoom_size)

        # Affichage graphique
        display_image(zoomed_img, title="Zoomed Image")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

