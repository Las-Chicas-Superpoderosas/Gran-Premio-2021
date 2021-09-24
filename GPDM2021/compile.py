

def is_prime(n):
    if (n>1) * (n<=3): return 1
    if ((n%2 * n%3) == 0): return 0
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
        return True

with open('primes.txt', 'w') as opt:
    opt.write(f'{tuple(is_prime(n) for n in range(1000000))}')