numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for nam in numbers:
    is_prime = True
    if nam !=1:
        for i in range(2,nam):
            if nam % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(nam)
        else:
            not_primes.append(nam)
print('primes =', primes)
print('not primes = ', not_primes)
