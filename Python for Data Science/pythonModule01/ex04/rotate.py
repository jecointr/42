# rotate.py
import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom_image(
    img_array: np.ndarray,
    x_start: int,
    y_start: int,
    width: int,
    height: int
) -> np.ndarray:

    """
    Crop a portion of the image (zoom) and return a single channel (red) image.
    """
    H, W, C = img_array.shape
    if C != 3:
        raise ValueError("Input image must have 3 channels (RGB)")

    if (
        x_start < 0
        or y_start < 0
        or x_start + width > W
        or y_start + height > H
    ):

        raise ValueError("Zoom area is out of image bounds")

    cropped = img_array[y_start:y_start+height, x_start:x_start+width, :]
    red_channel = cropped[:, :, 0][:, :, np.newaxis]  # (height, width, 1)
    return red_channel


def transpose_manual(img_array: np.ndarray) -> np.ndarray:
    """
    Manually transpose a 2D single-channel image (remove last dim if 1).
    """
    if img_array.shape[2] == 1:
        img_array_2d = img_array[:, :, 0]
    else:
        img_array_2d = img_array
    H, W = img_array_2d.shape
    transposed = np.zeros((W, H), dtype=img_array_2d.dtype)
    for i in range(H):
        for j in range(W):
            transposed[j, i] = img_array_2d[i, j]
    return transposed


def display_image(img_array: np.ndarray, title="Image"):
    """Display a 2D image with matplotlib."""
    plt.imshow(img_array, cmap='gray')
    plt.title(title)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()


def main():
    try:
        img_array = ft_load("animal.jpeg")
        H, W, C = img_array.shape

        # Zoom sur un carré 400x400
        zoom_size = 400
        x_start = max((W - zoom_size) // 2, 0)
        y_start = max((H - zoom_size) // 2, 0)
        zoomed_img = zoom_image(
            img_array,
            x_start,
            y_start,
            zoom_size,
            zoom_size,
        )

        # Affichage terminal
        print(
            "The shape of image is: "
            f"{zoomed_img.shape} or "
            f"({zoomed_img.shape[0]}, {zoomed_img.shape[1]})"
        )
        print(zoomed_img)

        # Transpose manuel
        transposed_img = transpose_manual(zoomed_img)
        print(f"New shape after Transpose: {transposed_img.shape}")
        print(transposed_img)

        # Affichage graphique
        display_image(transposed_img, title="Transposed Image")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
