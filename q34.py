#Print first 25 prime numbers

def print_primes(n):
    count = 0
    num = 2

    while count < n:
        is_prime = True
                        
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)
            count += 1

        num += 1
print_primes(25)