# from sys import stdin as inp
from sys import stdout as out

with open('input.txt', 'r') as inp:
    k, d = map(int, inp.readline().split())
    knights = set(range(1, k + 1))
    seats = {}
    for ln in inp.readlines():
        a, b = map(int, ln.split())
        seats[b] = a
        knights.discard(a)
    knights.difference_update(range(min(seats)))
    out.write(f'{len(knights) % (10**9 + 7)}')
out.write(f'{51251}')


class Node(dict):
    def __init__(self, data):
        super().__init__()
        self['data'] = data

    @property
    def data(self):
        return self['data']

    @property
    def nxt(self):
        return self['next']

class Linked_List(Node):
    def __init__(self, data, nxt=None):
        super().__init__()
        self['start'] = start

    @property
    def start(self):
        return self['start']
