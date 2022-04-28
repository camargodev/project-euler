def is_fully_divisible(number, max_divisor):
    divisor = max_divisor
    for divisor in range(max_divisor, 1, -1):
        if number % divisor != 0:
            return False
    return True

def find_smallest_valid_number(max_divisor):
    number = max_divisor
    while not is_fully_divisible(number, max_divisor):
        number += max_divisor
    return number

print(find_smallest_valid_number(20))