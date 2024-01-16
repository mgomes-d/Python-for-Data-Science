import sys

def check_argument():
    try:
        int(sys.argv[1])
        return True
    except ValueError:
        return False


def main():
    try:
        if len(sys.argv) < 2:
            return
        assert len(sys.argv) <= 2, "more than one argument is provided"
        assert check_argument(), "argument is not an integer"
        value = int(sys.argv[1])
        if value % 2:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    except AssertionError as msg:
        print("AssertionError:", msg)


if __name__ == "__main__":
    main()
