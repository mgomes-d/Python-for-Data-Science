
def ft_mean(array):
    try:
        result = 0
        index = 0
        for number in array:
            result += number
            index += 1
        result /= index
        return result
    except:
        print("ERROR")

def ft_median(array):
    try:
        array.sort()
        index = int(len(array) / 2)
        result = array[index]
        return result
    except:
        print("ERROR")

def ft_quartile(array):
    try:
        array.sort()
        index_25 = int(len(array) * 0.25)
        index_75 = int(len(array) * 0.75)
        result = []
        result.append(float(array[index_25]))
        result.append(float(array[index_75]))
        return result
    except:
        print("ERROR")

def ft_standard(array):
    try:
        mean = ft_mean(array)
        result = 0
        for i in range(len(array)):
            result += (array[i] - mean) **2
        result = (result / len(array))**0.5
        return result
    except:
        print("ERROR")

def ft_variance(array):
    try:
        result = ft_standard(array) ** 2
        return result
    except:
        print("ERROR")

def ft_statistics(*args: any, **kwargs: any) -> None:
    numbers = []
    for value in args:
        numbers.append(value)
    for key, value in kwargs.items():
        if value == "mean":
            result = 
            print(f'mean : {ft_mean(numbers)}')
        elif value == "median":
            result = 
            print(f'median : {ft_median(numbers)}')
        elif value == "quartile":
            result = 
            print(f'quartile : {ft_quartile(numbers)}')
        elif value == "var":
            result = 
            print(f'var : {ft_variance(numbers)}')
        elif value == "std":
            result = 
            print(f'std : {ft_standard(numbers)}')
