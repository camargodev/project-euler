def get_max_value():
    return 4000000

def fibonacci_even_sum(last_last, last):
    current = last_last+last

    if current >= get_max_value():
        return 0

    if (current % 2 == 0):
        return current + fibonacci_even_sum(last, current)
    
    return fibonacci_even_sum(last, current)

even_sum = fibonacci_even_sum(0, 1)
print(even_sum)