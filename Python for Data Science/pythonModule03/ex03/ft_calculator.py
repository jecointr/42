# ft_calculator.py
class calculator:
    """Classe permettant des calculs sur des vecteurs avec un scalaire."""

    def __init__(self, vector: list[float]):
        """Initialise le vecteur."""
        self.vector = vector

    def __add__(self, scalar: float) -> list[float]:
        """Additionne un scalaire à chaque élément du vecteur."""
        self.vector = [v + scalar for v in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, scalar: float) -> list[float]:
        """Soustrait un scalaire à chaque élément du vecteur."""
        self.vector = [v - scalar for v in self.vector]
        print(self.vector)
        return self.vector

    def __mul__(self, scalar: float) -> list[float]:
        """Multiplie chaque élément du vecteur par un scalaire."""
        self.vector = [v * scalar for v in self.vector]
        print(self.vector)
        return self.vector

    def __truediv__(self, scalar: float) -> list[float]:
        """
        Divise chaque élément du vecteur par un scalaire.
        Protège contre la division par zéro.
        """
        if scalar == 0:
            print("Erreur : division par zéro")
            return self.vector
        self.vector = [v / scalar for v in self.vector]
        print(self.vector)
        return self.vector
