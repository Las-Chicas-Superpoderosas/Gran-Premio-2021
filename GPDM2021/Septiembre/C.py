from sys import stdin, stdout


def cut(cards):
    counter = {'R': 0, 'B': 0}
    if cards[-1] == 'R':
        return 0
    for ind, card in enumerate(cards):
        counter[card] += 1
        if counter['R'] > counter['B']:
            return ind + 1
    return cards


n = int(stdin.readline())
for i in range(n):
    cards = stdin.readline().strip()
    stdout.write(f'{cut(cards)}\n')
