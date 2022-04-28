def square_of_sum(number):
    return sum(range(number+1))**2

def sum_of_squares(number):
    return sum(list(map(lambda x: x**2, range(number+1))))

def calculate_diff(number):
    return square_of_sum(number) - sum_of_squares(number)

print(calculate_diff(100))