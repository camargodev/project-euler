def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

def calculate_largest_product(number):
    largest_valid_product = 0
    for i in range(999, 100, -1):
        for j in range(i, 100, -1):
            product = i*j
            if is_largest_palindrome(product, number, largest_valid_product):
                largest_valid_product = max(largest_valid_product, product)
    return largest_valid_product

def is_largest_palindrome(product, number, current_largest):
    is_valid_product = product >= current_largest and product < number
    return is_valid_product and is_palindrome(product)

number_of_cases = int(input().strip())
for _ in range(number_of_cases):
    number = int(input().strip())
    print(calculate_largest_product(number))