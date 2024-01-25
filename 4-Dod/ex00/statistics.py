
def ft_mean(array):
    result = 0
    index = 0
    for number in array:
        result += number
        index += 1
    result /= index
    return result

def ft_median(array):
    array.sort()
    index = int(len(array) / 2)
    result = array[index]
    return result

def ft_quartile(array):
    array.sort()
    index_25 = int(len(array) * 0.25)
    index_75 = int(len(array) * 0.75)
    result = []
    result.append(float(array[index_25]))
    result.append(float(array[index_75]))
    return result

def ft_standard(array):
    mean = ft_mean(array)
    result = 0
    for i in range(len(array)):
        result += (array[i] - mean) **2
    result = (result / len(array))**0.5
    return result

def ft_variance(array):
    result = ft_standard(array) ** 2
    return result

def ft_statistics(*args: any, **kwargs: any) -> None:
    """take in *args a quantity of unknown number and make the Mean, Median,
    Quartile (25% and 75%), Standard Deviation and Variance according to the **kwargs
    ask.
    """
    numbers = []
    for value in args:
        numbers.append(value)
    for key, value in kwargs.items():
        try:
            if value == "mean":
                result = ft_mean(numbers)
                if result:
                    print(f'mean : {result}')
            elif value == "median":
                result = ft_median(numbers)
                if result:
                    print(f'median : {result}')
            elif value == "quartile":
                result = ft_quartile(numbers)
                if result:
                    print(f'quartile : {result}')
            elif value == "var":
                result = ft_variance(numbers)
                if result:
                    print(f'var : {result}')
            elif value == "std":
                result = ft_standard(numbers)
                if result:
                    print(f'std : {result}')
        except IndexError:
            print("ERROR")
        except ZeroDivisionError:
            print("ERROR")


