from math import sqrt

def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    factor = 3
    max_factor = sqrt(number)
    while factor <= max_factor:
        if number % factor == 0:
            return False
        factor += 2
    return True

def sum_primes(max_value):
    prime_sum = 2
    current_number = 3
    while current_number < max_value:
        if is_prime(current_number):
            prime_sum += current_number
        current_number += 2
    return prime_sum

print(sum_primes(2000000))