from math import sqrt

class CachedPrimes:
    def __init__(self):
        self.cache = [2]

    def get_starter_prime(self):
        return 1 if len(self.cache) == 1 else self.cache[-1]

    def has_nth_prime_cached(self, n):
        return len(self.cache) >= n

    def save_prime(self, prime):
        self.cache.append(prime)
    
    def get_nth_prime(self, n):
        return self.cache[n-1]

    def get_cache_length(self):
        return len(self.cache)

MIN_PRIME_FACTOR = 2

def is_prime(number):
    factor = MIN_PRIME_FACTOR
    max_factor = sqrt(number)
    while factor <= max_factor:
        if number % factor == 0:
            return False
        factor += 1
    return True

def calculate_nth_prime(n, cached_primes):
    prime_counter = cached_primes.get_cache_length()
    current = cached_primes.get_starter_prime()
    
    while prime_counter < n:
        current += 2
        if is_prime(current):
            cached_primes.save_prime(current)
            prime_counter += 1
    return current

def get_nth_prime(n, cached_primes):
    if cached_primes.has_nth_prime_cached(n):
        return cached_primes.get_nth_prime(n)
    return calculate_nth_prime(n, cached_primes)

number_of_cases = int(input().strip())
cached_primes = CachedPrimes()
for _ in range(number_of_cases):
    number = int(input().strip())
    print(get_nth_prime(number, cached_primes))