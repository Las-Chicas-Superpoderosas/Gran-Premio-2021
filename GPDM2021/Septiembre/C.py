from sys import stdin, stdout


def validate(cards):
    counter = 0
    for card in cards:
        counter += card
        if counter > 0:
            return False
    return True


def cut(cards):
    for ind in range(len(cards)):
        if validate(cards[ind:] + cards[:ind]):
            return ind
    return -1


n = int(stdin.readline())
for i in range(n):
    cards = tuple(
        map(
            lambda x: 1 if x == 'R' else -1,
            stdin.readline().strip()
        )
    )
    stdout.write(f'{cut(cards)}\n')
