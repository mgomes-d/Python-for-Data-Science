class calculator:

    def __init__(self, array):
        self.object = array

    def __add__(self, object) -> None:
        self.object = [item + object for item in self.object]
        print(self.object)
    def __mul__(self, object) -> None:
        self.object = [item * object for item in self.object]
        print(self.object)
    def __sub__(self, object) -> None:
        self.object = [item - object for item in self.object]
        print(self.object)
    def __truediv__(self, object) -> None:
        try:
            self.object = [item / object for item in self.object]
            print(self.object)
        except ZeroDivisionError as msg:
            print(msg)