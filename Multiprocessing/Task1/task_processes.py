from concurrent.futures import ProcessPoolExecutor
from time import perf_counter

from primes import is_prime
from primes_task_data import NUMBERS   # твій список

start = perf_counter()

with ProcessPoolExecutor() as executor:
    results = list(executor.map(is_prime, NUMBERS))

end = perf_counter()

print("ProcessPoolExecutor result:")
print(results)
print("Time:", end - start)
