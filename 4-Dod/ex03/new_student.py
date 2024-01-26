import random
import string
from dataclasses import dataclass, field

def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k = 15))

@dataclass
class Student:
    name: str = field(init = True)
    surname: str = field(init = True)
    activate: str = field(default = True)
    login: str = field(init = False)
    
    def __post_init__(self):
        self.login = self.name[0].capitalize() + self.surname.lower()

    id: str = field(default = generate_id(), init=False)