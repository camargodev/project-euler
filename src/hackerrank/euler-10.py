def sum_primes(N):
    sum_of_primes = [0,0]
    array = [i for i in range(N+1)]
    array[0] = 0
    array[1] = 0

    for number in range(2, N+1):
        if array[number] != 0:
            sum_of_primes.append(sum_of_primes[-1]+number)
            multiple = number**2
            while multiple <= N:
                array[multiple] = 0
                multiple += number
        else:
            sum_of_primes.append(sum_of_primes[-1])
    return sum_of_primes

number_of_cases = int(input().strip())
values = []
for _ in range(number_of_cases):
    value = int(input().strip())
    values.append(value)

prime_array = sum_primes(max(values))

for value in values:
    print(prime_array[value])
