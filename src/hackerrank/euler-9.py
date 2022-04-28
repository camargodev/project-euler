def find_triplet(N):
    max_product = -1
    N_sq = N**2
    for a in range(3,N//3):
        b = int((N_sq - 2*N*a)/(2*(N-a)))
        c = N - a - b
        if c**2 == a**2 + b**2:
            max_product = max(max_product, a*b*c)
    return max_product

number_of_cases = int(input().strip())
for _ in range(number_of_cases):
    total = int(input().strip())
    product = find_triplet(total)
    print(product)