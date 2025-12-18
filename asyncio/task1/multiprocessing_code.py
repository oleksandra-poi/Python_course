from multiprocessing import Pool
import time

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def square(n):
    return n * n

def cube(n):
    return n * n * n

if __name__ == "__main__":
    numbers = list(range(1, 11))

    start = time.time()

    with Pool() as pool:
        fibs = pool.map(fibonacci, numbers)
        facts = pool.map(factorial, numbers)
        squares = pool.map(square, numbers)
        cubes = pool.map(cube, numbers)

    end = time.time()

    print("Fibonacci:", fibs)
    print("Factorial:", facts)
    print("Squares:", squares)
    print("Cubes:", cubes)
    print("Multiprocessing time:", end - start)
