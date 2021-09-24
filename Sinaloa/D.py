from sys import stdin as inp, stdout as out

def digit_sum(n, i=0):
  while n:
    i += n%10
    n //= 10
  return i

lns = inp.read().splitlines()
for ln in lns[1:]:
  l, r = map(int, ln.split())
  out.write(f'{sum(map(digit_sum, range(l, r + 1)))}\n')
