def is_divisible(number):
    return number % 3 == 0 or number % 5 == 0

def calculate_sum(max_number):
    total = 0
    for number in range(max_number):
        if is_divisible(number):
            total += number
    return total


vals = [1000]
for val in vals:
    print(calculate_sum(val))