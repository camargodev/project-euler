def fibonacci_even_sum(max_value, last_last, last):
    current = last_last+last

    if current >= max_value:
        return 0

    if (current % 2 == 0):
        return current + fibonacci_even_sum(max_value, last, current)
    
    return fibonacci_even_sum(max_value, last, current)

number_of_cases = int(input().strip())

for _ in range(number_of_cases):
    max_number = int(input().strip())
    print(fibonacci_even_sum(max_number, 0, 1))