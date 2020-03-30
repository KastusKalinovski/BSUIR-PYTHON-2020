def cached(func_to_decorate):
    memo = {}

    def wrapper(*args):
        print("Function call with {}".format(args))
        if args in memo:
            print("Returning cached data...")
            return memo[args]
        else:
            print("Caching data...")
            val = func_to_decorate(*args)
            memo[args] = val
            return val

    return wrapper


@cached
def find_max(*args):
    return max(args)

