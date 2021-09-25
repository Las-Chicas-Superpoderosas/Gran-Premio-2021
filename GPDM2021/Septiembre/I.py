from sys import stdin, stdout

def multiPers(num):
    count = 0
    if num == 0:
        return count
    if num < 10:
        return count
    m = 1
    while num > 0:
        m *= num % 10
        num //= 10
    count += multiPers(m)
    return count + 1

t = int(stdin.readline())
for _ in range(t):
    num = int(stdin.readline())
    stdout.write(f'{multiPers(num)}\n')
