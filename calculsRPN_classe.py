import math


class Pile:
    def __init__(self):
        self._mapile = []

    def __str__(self):
        return str(self._mapile)[:-1] + "<"

    def __len__(self):
        return len(self._mapile)

    def sommet(self):
        if len(self) > 0:
            return self._mapile[-1]

    def empiler(self, contenu):
        self._mapile += [contenu]

    def depiler(self):
        if len(self) > 0:
            return self._mapile.pop()


class Rpn:
    def _add(a, b):
        return a + b

    def _sub(a, b):
        return a - b

    def _mul(a, b):
        return a * b

    def _div(a, b):
        return a / b

    def _neg(a):
        return -a

    def __init__(self, expression):
        self._mapile = Pile()
        self._liste_car = expression.split()
        self._analyse()

    def __str__(self):
        return str(self._mapile)

    def _analyse(self):
        dico_op_bin = {"+": Rpn._add, "-": Rpn._sub,
                       "*": Rpn._mul, "/": Rpn._div}
        dico_op_un = {"sin": math.sin, "cos": math.cos,
                      "neg": Rpn._neg, "log": math.log10,
                      "ln": math.log}

        for car in self._liste_car:
            car = car.lower()
            if car in dico_op_bin:
                a, b = self._depile2()
                self._mapile.empiler(dico_op_bin[car](a, b))
            elif car in dico_op_un:
                a = self._mapile.depiler()
                self._mapile.empiler(dico_op_un[car](a))
            else:
                self._mapile.empiler(float(car))

    def _depile2(self):
        nb1 = self._mapile.depiler()
        nb2 = self._mapile.depiler()
        return nb2, nb1


if __name__ == "__main__":

    expressions = ["2 3 7 - *",
                   "10 4 - 5 7 + *",
                   "10 4 - 5 7 + 5 7 + * /",
                   "3 2 / 2 - 4 3 / 1 2 / + /",
                   "2.7183 LN"]
    for c in expressions:
        rc = Rpn(c)
        print(rc)
