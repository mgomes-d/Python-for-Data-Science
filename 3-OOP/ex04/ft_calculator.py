class calculator:
    #your code here
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        #your code here
        result = [a * b for a, b in zip(V1, V2)]
        print(f'Dot product is: {sum(result)}')
    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        result = [a + b for a, b in zip(V1, V2)]
        print(f'Add Vector is : {result}')
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        result = [a - b for a, b in zip(V1, V2)]
        print(f'Sous Vector is: {result}')
