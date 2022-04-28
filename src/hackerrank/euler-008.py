def calculate_product_of_size_n(string, n, starter_index=0):
  if starter_index+n >= len(string):
    return 0, starter_index

  product = 1
  for index in range(starter_index, starter_index+n):
    product *= int(string[index])

  if product == 0:
    return calculate_product_of_size_n(string, n, starter_index+1)

  return product, starter_index


def calculate_current_product(previous_product, index, string, n):
  digit = int(string[index])

  if digit == 0:
    current_product, index = calculate_product_of_size_n(string, n, index+1)
    return current_product, index+n

  digit_to_remove = int(string[index-n])
  current_product = previous_product * digit // digit_to_remove
  return current_product, index+1


def calculate_largest_product_of_size_n(string, n):
  current_product, index = calculate_product_of_size_n(string, n)
  max_product = current_product

  index += n
  while index < len(string):
    current_product, index = calculate_current_product(current_product, index, string, n)
    max_product = max(current_product, max_product)
  
  return max_product


number_of_cases = int(input().strip())
for _ in range(number_of_cases):
    _, product_length = input().strip().split(' ')
    product_length = int(product_length)
    number = input().strip()
    print(calculate_largest_product_of_size_n(number, product_length))