import numpy as np


def ft_invert(array: np.ndarray) -> np.ndarray:
    """
    Inverts the color of the image received.
    """
    return 255 - array  # = et - utilisés


def ft_red(array: np.ndarray) -> np.ndarray:
    """
    Keep only the red channel, zero out green and blue.
    """
    result = array.copy()
    result[:, :, 1] = 0  # vert
    result[:, :, 2] = 0  # bleu
    return result  # = utilisé


def ft_green(array: np.ndarray) -> np.ndarray:
    """
    Keep only the green channel, zero out red and blue.
    """
    result = array.copy()
    result[:, :, 0] = 0  # rouge
    result[:, :, 2] = 0  # bleu
    return result  # = utilisé


def ft_blue(array: np.ndarray) -> np.ndarray:
    """
    Keep only the blue channel, zero out red and green.
    """
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """
    Convert image to grayscale using average of RGB.
    """
    # Convertir en float pour la division, puis revenir à uint8
    grey = ((array[:, :, 0].astype(np.float32) +
             array[:, :, 1].astype(np.float32) +
             array[:, :, 2].astype(np.float32)) / 3).astype(np.uint8)

    # Répliquer sur les 3 canaux pour garder la forme (H, W, 3)
    result = np.stack([grey, grey, grey], axis=2)
    return result
