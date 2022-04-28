def square_of_sum(n):
    return (n*(n+1) // 2)**2

def sum_of_squares(n):
    return (n*(n+1)*(2*n+1)) // 6

def calculate_diff(number):
    return square_of_sum(number) - sum_of_squares(number)

number_of_cases = int(input().strip())
for _ in range(number_of_cases):
    number = int(input().strip())
    print(calculate_diff(number))