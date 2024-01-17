def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing: None", type(object))
    elif isinstance(object, float):
        if object != object:
            print("Cheese: nan", type(object))
        else:
            print("Type not found")
            return 1
    elif isinstance(object, int) and object != False:
        if object == 0:
            print("Zero: 0", type(object))
        else:
            print("Type not found")
            return 1
    elif isinstance(object, str):
        if object == "":
            print("Empty:", type(object))
        else:
            print("Type not found")
            return 1
    elif isinstance(object, bool):
        if object is not True:
            print("Fake: False", type(object))
        else:
            print("Type not found")
            return 1
    else:
        print("Type not found")
            return 1
    return 0
