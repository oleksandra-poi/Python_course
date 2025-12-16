from concurrent.futures import ThreadPoolExecutor
from time import perf_counter

from primes import is_prime

NUMBERS = [
   2,
   1099726899285419,
   1570341764013157,
   1637027521802551,
   1880450821379411,
   1893530391196711,
   2447109360961063,
   3,
   2772290760589219,
   3033700317376073,
   4350190374376723,
   4350190491008389,
   4350190491008390,
   4350222956688319,
   2447120421950803,
   5,
]


start = perf_counter()

with ThreadPoolExecutor() as executor:
    results = list(executor.map(is_prime, NUMBERS))

end = perf_counter()

print("ThreadPoolExecutor result:")
print(results)
print("Time:", end - start)
