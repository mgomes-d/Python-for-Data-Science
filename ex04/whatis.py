import sys


def main():
    try:
        if len(sys.argv) < 2:
            return
        assert len(sys.argv) <= 2, "more than one argument is provided"
        value = int(sys.argv[1])
        if value % 2:
            print("I'm Odd.")
        else:
            print("I'm Even.")
    except AssertionError as msg:
        print("AssertionError:", msg)
    except ValueError:
        print("AssertionError: argument is not an integer")


if __name__ == "__main__":
    main()
