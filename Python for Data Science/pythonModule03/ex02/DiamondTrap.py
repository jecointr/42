# DiamondTrap.py
from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    Classe représentant un roi combinant les caractéristiques
    des familles Baratheon et Lannister.
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """
        Initialise le roi avec prénom, état de vie et caractéristiques
        héritées.
        """
        # On appelle le constructeur de Baratheon
        # (le premier parent dans l'ordre MRO)
        Baratheon.__init__(self, first_name, is_alive)

    # Properties pour les yeux
    def get_eyes(self):
        """Retourne la couleur des yeux."""
        return self.eyes

    def set_eyes(self, color: str):
        """Change la couleur des yeux."""
        self.eyes = color

    # Properties pour les cheveux
    def get_hairs(self):
        """Retourne la couleur des cheveux."""
        return self.hairs

    def set_hairs(self, color: str):
        """Change la couleur des cheveux."""
        self.hairs = color
