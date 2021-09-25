from sys import stdin, stdout

a, b = map(int, stdin.readline().split())
area_kg = 30
a = tuple(int(x) for x in stdin.read().rsplit(' '))
stdout.write(f'{n*a}')