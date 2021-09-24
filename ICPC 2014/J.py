from sys import stdin as inp, stdout as out


def bfs(graph, node_A, node_B):
    visited = set()

    queue = [[node_A, 0]]
    visited.add(str(node_A))

    while len(queue):
        [node, distance] = queue.pop(0)
        if node == node_B:
            return distance
        for neighbor in graph[node]:
            if str(neighbor) not in visited:
                visited.add(str(neighbor))
                queue.append([neighbor, (distance + 1)])
    return -1


class Travel(object):
    def __init__(self, r, c, n, carriage_system):
        self.r, self.c, self.n = r, c, n
        self.carriage_system = carriage_system

    def get_costs(self):
        self.costs = {i: {} for i in range(self.r)}
        for ind, line in enumerate(self.carriage_system):
            sect, i = ind // self.r, ind % self.r
            for j, val in enumerate(map(int, line.split())):
                self.costs[sect][f'{i} {j}'] = val

    def smallest_cost(self):
        out.write(f'{0}')


r, c, n = map(int, inp.readline().split())
carriage_system = inp.readlines(r * 3)

travel = Travel(r, c, n, carriage_system)
travel.get_costs()
travel.smallest_cost()
