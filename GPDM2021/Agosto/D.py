from sys import stdin, stdout


class Cocina(object):
    def __init__(self, pizzas):
        self.e1 = Esclavo(0)
        self.e2 = Esclavo(1)
        self.e3 = Esclavo(2)
        self.e4 = Esclavo(3)
        self.pizzas = pizzas
        self.time = 0

    def employees(self):
        return (self.e1, self.e2, self.e3, self.e4)

    def clean(self):
        if pizzas[0].done:
            pizzas.remove(pizzas[0])

    @property
    def working(self):
        return False in map(lambda x: x.done, self.pizzas)

    def find_pizza(self, i):
        for pizza in self.pizzas:
            if pizza[i] and (i == 0 or sum(pizza[:i]) == 0):
                return pizza
        return None

    def work(self):
        w_pizzas = []
        for e in self.employees():
            if e.pizza is None or not e.pizza[e.ing]:
                e.pizza = self.find_pizza(e.ing)
            w_pizzas.append(e.pizza)
        for e in self.employees():
            e.work()
        self.time += 1
        self.clean()

    def __repr__(self) -> str:
        return '\n'.join(map(str, self.pizzas))


class Pizza(list):
    def __init__(self, i1, i2, i3, i4):
        super()
        self.extend((i1, i2, i3, i4))

    @property
    def done(self):
        return sum(self) == 0

    def __repr__(self) -> str:
        return ', '.join(map(str, self))


class Esclavo(object):
    def __init__(self, ing):
        self.ing = ing
        self.pizza = None

    def work(self):
        if self.pizza:
            self.pizza[self.ing] -= 1


with open('input.txt', 'r') as stdin:
    n = int(stdin.readline())
    pizzas = list(Pizza(*map(int, stdin.readline().split())) for _ in range(n))
    cocina = Cocina(pizzas)
    while cocina.working:
        cocina.work()
    stdout.write(f'{cocina.time}')
