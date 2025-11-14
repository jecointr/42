# ft_calculator.py

class calculator:
    """Classe pour effectuer des opérations sur des vecteurs."""

    def __init__(self, vector: list[float]):
        """Initialise le vecteur."""
        self.vector = vector

    # Exercice 03: opérations sur vecteur + scalaire
    def __add__(self, scalar: float):
        self.vector = [v + scalar for v in self.vector]
        print(self.vector)
        return self.vector

    def __sub__(self, scalar: float):
        self.vector = [v - scalar for v in self.vector]
        print(self.vector)
        return self.vector

    def __mul__(self, scalar: float):
        self.vector = [v * scalar for v in self.vector]
        print(self.vector)
        return self.vector

    def __truediv__(self, scalar: float):
        if scalar == 0:
            print("Erreur : division par zéro")
            return self.vector
        self.vector = [v / scalar for v in self.vector]
        print(self.vector)
        return self.vector

    # Exercice 04: opérations sur 2 vecteurs
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]):
        """Produit scalaire de deux vecteurs."""
        result = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print(f"Dot product is: {result}")
        return result

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]):
        """Addition élément par élément de deux vecteurs."""
        result = [float(v1 + v2) for v1, v2 in zip(V1, V2)]
        print(f"Add Vector is : {result}")
        return result

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]):
        """Soustraction élément par élément de deux vecteurs."""
        result = [float(v1 - v2) for v1, v2 in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
        return result

