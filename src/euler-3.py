def get_number():
    return 600851475143

def get_first_prime_factor(number):
    for factor in range(2, number):
        if number % factor == 0:
            return factor
    return number

def get_max_prime_factor_rec(number):
    first_prime = get_first_prime_factor(number)
    if number == first_prime:
        return number
    return get_max_prime_factor_rec(int(number / first_prime))

print(get_max_prime_factor_rec(get_number()))
