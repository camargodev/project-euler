def find_triplet(total_sum):
    for a in range(total_sum):
        for b in range(a+1, total_sum):
            c = total_sum - a - b
            if c <= a or c <= b:
                continue
            if c**2 == (a**2 + b**2):
                return a, b, c
    return 0, 0, 0

a, b, c = find_triplet(1000)
print(a*b*c)