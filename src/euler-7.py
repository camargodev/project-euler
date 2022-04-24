MIN_PRIME_FACTOR = 2

def is_prime(number):
    factor = MIN_PRIME_FACTOR
    max_factor = number // factor
    while factor <= max_factor:
        if number % factor == 0:
            return False
        factor += 1
        max_factor = number // factor    
    return True

def get_nth_prime(n):
    prime_counter = 0
    current = 1
    while prime_counter < n:
        current += 1
        if is_prime(current):
            prime_counter += 1 
    return current

print(get_nth_prime(3))
        