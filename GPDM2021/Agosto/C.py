from sys import stdin, stdout

MAX = 1000000

primes = set(range(2, MAX))
nprimes = [0] * (MAX +1)
c = 0
for i in range(2, MAX +2):
    if i in primes:
        c+=1
        primes.difference_update(set(range(i+i, MAX, i)))
    nprimes[i] = c

n = int(stdin.readline())
for _ in range(n):
    m, M = map(int, stdin.readline().split())
    stdout.write(f"{nprimes[M] - nprimes[m]}\n")
