MIN_PRIME_FACTOR = 2

def get_first_prime_factor(number):
    factor = MIN_PRIME_FACTOR
    max_factor = number // factor
    while factor <= max_factor:
        if number % factor == 0:
            return factor
        factor += 1
        max_factor = number // factor
        
    return number

def get_max_prime_factor(number):
    first_prime = get_first_prime_factor(number)
    if number == first_prime:
        return number
    return get_max_prime_factor(number // first_prime)

number_of_cases = int(input().strip())
for _ in range(number_of_cases):
    number = int(input().strip())
    print(get_max_prime_factor(number))