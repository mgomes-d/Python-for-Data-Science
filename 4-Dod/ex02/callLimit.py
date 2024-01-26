def callLimit(limit: int):
    count = 0
    def callLimiter(function):
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            try:
                count += 1
                assert count <= limit, f"function {function} call too many times"
                return function(*args, **kwds)
            except AssertionError as msg:
                print("Error:", msg)

        return limit_function
    return callLimiter
            