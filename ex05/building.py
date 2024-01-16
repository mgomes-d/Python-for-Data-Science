import sys


def get_parameters(string, func):
    i = 0
    if isinstance(func, str) is not True:
        for char in string:
            if func(char) == True:
                i += 1
    else:
        for char in string:
            if char in func:
                i += 1
    return i

def building(text):
    punctuation = "!" + '"' + "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    print(f'The text contains {len(text)} characters:')
    print(f'- {get_parameters(text, str.isupper)} upper letters')
    print(f'- {get_parameters(text, str.islower)} lower letters')
    print(f'- {get_parameters(text, punctuation)} punctuation marks')
    print(f'- {get_parameters(text, str.isspace)} spaces')
    print(f'- {get_parameters(text, str.isdigit)} digits')

def main():
    try:
        if len(sys.argv) <= 1:
            string = input("What is the text to count?\n")
            building(string)
            return 0
        assert len(sys.argv) <= 2, "more than one argument is provided"
        building(sys.argv[1])
    except AssertionError as msg:
        print("AssertionError:", msg)

if __name__ == "__main__":
    main()