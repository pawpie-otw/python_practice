import time


def timeit_wrapper(func):

    def wrapper(*args, **kwargs):
        time_start = time.time()
        result = func(*args, **kwargs)
        print("executed time:", time.time()-time_start)
        return result
    return wrapper


@timeit_wrapper
def fib(n: int) -> int:

    if n < 1:
        return -1

    if n < 3:
        return fib_array[n]

    fib_array = [int(1), int(1)]
    for _ in range(n-2):
        fib_array[0], fib_array[1] = fib_array[1], fib_array[0]+fib_array[1]
    return fib_array[1]


print(fib(1_000_000))
