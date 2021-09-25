from sys import stdin, stdout


def max_spoons(C, R, S):
    min_perfect_scoops = S - R if S > R else 0
    return C // S, min_perfect_scoops


n = int(stdin.readline())
for i in range(n):
    C, R, S = map(int, stdin.readline().split())
    max_spoon, min_spoon = max_spoons(C, R, S)
    stdout.write(f'{max_spoon} {min_spoon}\n')
