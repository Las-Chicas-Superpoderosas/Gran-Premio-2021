from sys import stdin, stdout
def power_of_two(k):
    if k == 1:
        return "2"
    if k % 2:
        return "(2*" + power_of_two(k-1)+ ")"
    return "("+power_of_two(k>>1) +")^2" 

n = int(stdin.readline())
for _ in range(n):
    x = int(stdin.readline())
    stdout.write(f"{power_of_two(x)}\n")
