import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random 15-character ID using lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Dataclass representing a student.

    Attributes:
        name: Student's first name
        surname: Student's surname
        active: Whether the student is active (default True)
        login: Auto-generated login from surname (capitalized)
        id: Auto-generated random ID
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Initialize login and id after object creation."""
        self.login = (self.name[0] + self.surname).capitalize()
        self.id = generate_id()
