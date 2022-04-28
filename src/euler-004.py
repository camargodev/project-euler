def is_palindrome(number):
    str_num = str(number)
    return str_num == str_num[::-1]

def calculate_largest_product():
    largest_product = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            product = i*j
            if is_palindrome(product):
                largest_product = max(largest_product, product)
    return largest_product

print(calculate_largest_product())