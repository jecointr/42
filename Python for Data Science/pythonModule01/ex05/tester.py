# tester.py
from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib.pyplot as plt


def display_image(img_array, title="Image"):
    """Affiche l'image avec matplotlib"""
    plt.imshow(img_array)
    plt.title(title)
    plt.axis('off')
    plt.show()


def main():
    try:
        # Charger l'image
        array = ft_load("landscape.jpg")
        print(f"The shape of image is: {array.shape}")
        print(array)

        # Appliquer les filtres
        inverted = ft_invert(array)
        red = ft_red(array)
        green = ft_green(array)
        blue = ft_blue(array)
        grey = ft_grey(array)

        # Affichage graphique
        display_image(array, title="Original")
        display_image(inverted, title="Invert")
        display_image(red, title="Red")
        display_image(green, title="Green")
        display_image(blue, title="Blue")
        display_image(grey, title="Grey")

        # Afficher la docstring de la première fonction
        print(ft_invert.__doc__)

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
