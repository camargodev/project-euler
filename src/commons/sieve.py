from math import sqrt

def create_array(N):
    array = [True] * (N+1)
    array[0] = False
    array[1] = False

    for number in range(2, N):
        if array[number] == True:
            multiple = 2*number
            while multiple <= N:
                array[multiple] = False
                multiple += number
        
    return array

def sum_primes(N):
    sum_of_primes = [0,0]
    array = [i for i in range(N+1)]
    array[0] = 0
    array[1] = 0

    for number in range(2, int(sqrt(N))+1):
        if array[number] != 0:
            sum_of_primes.append(sum_of_primes[-1]+number)
            multiple = 2*number
            while multiple <= N:
                array[multiple] = 0
                multiple += number
        else:
            sum_of_primes.append(sum_of_primes[-1])
    
    return sum_of_primes

# N = 30
# x = [i for i in range(N+1)]
# print(x)

# print(create_array(30))
print(sum_primes(5))