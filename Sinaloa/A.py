from sys import stdin as inp, stdout as out

    # with open('./input.txt', 'r') as inp:
n = int(inp.readline())
n2 = n >> 1
a = tuple(int(x) for x in inp.readline().split())
b, c = sum(a[:n2]), sum(a[n2 + n%2:])
out.write(f'{b + (c * (b != c)) + (a[n2] * n%2)} {int(b==c)}')
