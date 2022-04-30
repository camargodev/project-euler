def get_grid():
    grid = []
    for _ in range(20):
        str_line = input().strip().split(' ')
        line = [int(element) for element in str_line]
        grid.append(line)

    return grid


def calculate_max_product_of_size_n(grid, n):
  max_product = 0

  number_of_lines = len(grid)
  for line in range(number_of_lines):

    number_of_columns = len(grid[line])
    for column in range(number_of_columns):
      product_right, product_down, product_upper_diagonal, product_lower_diagonal = 1, 1, 1, 1

      for offset in range(n):
        right_offset = column+offset
        down_offset = line+offset
        up_offset = line-offset

        is_valid_right_offset = right_offset < number_of_columns
        is_valid_down_offset = down_offset < number_of_lines
        is_valid_up_offset = up_offset >= 0

        product_right *= grid[line][right_offset] if is_valid_right_offset else 0
        product_down *= grid[down_offset][column] if is_valid_down_offset else 0
        product_upper_diagonal *= grid[up_offset][right_offset] if is_valid_right_offset and is_valid_up_offset else 0
        product_lower_diagonal *= grid[down_offset][right_offset] if is_valid_right_offset and is_valid_down_offset else 0

      max_product = max(max_product, product_right, product_down, product_lower_diagonal, product_upper_diagonal)

  return max_product


print(calculate_max_product_of_size_n(get_grid(), 4))