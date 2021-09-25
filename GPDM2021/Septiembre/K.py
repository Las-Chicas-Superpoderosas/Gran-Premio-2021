from sys import stdin, stdout

def binary_repeat(k):
    if (k%2):
        return 0
    mx = int('1' * k, base=2)
    nums = (bin(i)[2:].zfill(k) for i in range(mx + 1))
    count = 0
    for n in nums:
        ks = k>>1
        while ks:
            if (n[:ks]*(k//ks) == n):
                count += 1
                break
            ks >>= 1
    return count


n = int(stdin.readline())
for _ in range(n):
    k = int(stdin.readline())
    stdout.write(f'{binary_repeat(k)}\n')
