from abc import ABC, abstractmethod

class Character(ABC):
    """Class character with contructor and die method"""
    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """Contructor for character, need 2 arguments:
        first_name(string)
        is_alive(bool), default at true"""
        self.first_name = str(first_name)
        self.is_alive = bool(is_alive)
    @abstractmethod
    def die(self):
        pass

class Stark(Character):
    """Stark class"""
    def __init__(self, first_name, is_alive=True):
        """Stark constructor"""
        self.first_name = str(first_name)
        self.is_alive = bool(is_alive)
    def die(self):
        """killing Stark"""
        self.is_alive = False