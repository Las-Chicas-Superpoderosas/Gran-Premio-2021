from functools import lru_cache
from sys import stdin, stdout


DIR = ((-1, -1),
       (-1,  0),
       (-1,  1),
       (0, -1),
       (0,  1),
       (1, -1),
       (1,  0),
       (1,  1))


class XYPlane(dict):
    def __init__(self):
        super().__init__()

    def coord(self, x, y, val=None):
        try:
            if val:
                self[f'{x} {y}'] = val
            return self[f'{x} {y}']
        except KeyError:
            return None


def find_max(plane, MIN, MAX):
    def neighbors(x, y):
        return ((x+dx, y+dy) for dx, dy in DIR if f'{x+dx} {y+dy}' in plane)
    
    @lru_cache(MIN*MAX)
    def has_next(crd):
        x, y = map(int, crd.split())
        val = plane[crd]
        for ncrd in neighbors(x, y):
            if plane.coord(*ncrd) == val + 1:
                return f'{ncrd[0]} {ncrd[1]}'
        return False

    def count_streak(crd, streak):
        n_crd = has_next(crd)
        return count_streak(n_crd, streak + 1) if n_crd else streak

    MAX_STREAK = MAX-MIN
    max_streak = 0
    for coord, v in plane.items():
        if max_streak > MAX-v:
            continue
        streak = count_streak(coord, 1)
        max_streak = max_streak if max_streak > streak else streak
        if max_streak == MAX_STREAK:
            break
    return max_streak


N, M = map(int, stdin.readline().split())
plane = XYPlane()
min_n, max_n = 26, 0
for n in range(N):
    for m, v in enumerate(map(lambda x: ord(x)-64, stdin.readline().strip())):
        plane.coord(n, m, val=v)
        min_n = v if min_n > v else min_n
        max_n = v if max_n < v else max_n

stdout.write(f'{find_max(plane, min_n, max_n)}')
