def get_number():

  string = ""
  string += "73167176531330624919225119674426574742355349194934"
  string += "96983520312774506326239578318016984801869478851843"
  string += "85861560789112949495459501737958331952853208805511"
  string += "12540698747158523863050715693290963295227443043557"
  string += "66896648950445244523161731856403098711121722383113"
  string += "62229893423380308135336276614282806444486645238749"
  string += "30358907296290491560440772390713810515859307960866"
  string += "70172427121883998797908792274921901699720888093776"
  string += "65727333001053367881220235421809751254540594752243"
  string += "52584907711670556013604839586446706324415722155397"
  string += "53697817977846174064955149290862569321978468622482"
  string += "83972241375657056057490261407972968652414535100474"
  string += "82166370484403199890008895243450658541227588666881"
  string += "16427171479924442928230863465674813919123162824586"
  string += "17866458359124566529476545682848912883142607690042"
  string += "24219022671055626321111109370544217506941658960408"
  string += "07198403850962455444362981230987879927244284909188"
  string += "84580156166097919133875499200524063689912560717606"
  string += "05886116467109405077541002256983155200055935729725"
  string += "71636269561882670428252483600823257530420752963450"

  return string


def calculate_product_of_size_n(n, starter_index=0):
  string = get_number()
  product = 1
  is_valid_product = False

  while not is_valid_product and starter_index+n < len(string):
    for index in range(starter_index, starter_index+n):
      product *= int(string[index])

    if product == 0:
      starter_index += 1
      product = 1
    else:
      is_valid_product = True 

  return product, starter_index


def calculate_largest_product_of_size_n(n):
  string = get_number()
  current_product, index = calculate_product_of_size_n(n)
  max_product = current_product

  index += n
  while index < len(string):
    digit = int(string[index])
    
    if digit == 0:
      current_product, index = calculate_product_of_size_n(n, index+1)
      index += n
    else:
      digit_to_remove = int(string[index-n])
      current_product = current_product * digit // digit_to_remove
      index += 1

    max_product = max(current_product, max_product)
  
  return max_product


print(calculate_largest_product_of_size_n(13))