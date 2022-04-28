from math import floor

def calculate_multiples_sum(max_number, multiples_of):
    n = floor((max_number-1)/multiples_of)+1
    a1 = 0
    an = a1 + (n-1)*multiples_of
    return int(n*(a1+an)/2)

def calculate_sum(max_number):
    sum3 = calculate_multiples_sum(max_number, multiples_of=3)
    sum5 = calculate_multiples_sum(max_number, multiples_of=5)
    sum15 = calculate_multiples_sum(max_number, multiples_of=15)
    return sum3 + sum5 - sum15

number_of_cases = int(input().strip())

for _ in range(number_of_cases):
    max_number = int(input().strip())
    print(calculate_sum(max_number))