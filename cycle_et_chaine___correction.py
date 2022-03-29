class Pile:
    def __init__(self):
        self._pile = []

    def __len__(self):
        return len(self._pile)

    def empiler(self, element):
        self._pile.append(element)

    def depiler(self):
        if len(self) != 0:
            return self._pile.pop()

    def est_vide(self):
        return len(self) == 0


class File:
    def __init__(self):
        self._file = []

    def __len__(self):
        return len(self._file)

    def enfiler(self, element):
        self._file.append(element)

    def defiler(self):
        if len(self) != 0:
            return self._file.pop(0)

    def est_vide(self):
        return len(self) == 0


def cycle(G):
    p = Pile()
    p.empiler(0)

    ordre = len(G[0])
    visites = [False] * ordre

    while not p.est_vide():
        s = p.depiler()

        for i in range(ordre):
            v = G[s][i]
            if v == 1 and not visites[i]:
                p.empiler(i)

        if visites[s]:
            return True
        else:
            visites[s] = True

    return False


def est_une_chaine(G, A, B):
    f = File()
    f.enfiler(A)

    ordre = len(G[0])
    visites = [False] * ordre

    while not f.est_vide():
        s = f.defiler()
        visites[s] = True

        for i in range(ordre):
            v = G[s][i]
            if v == 1:
                if i == B:
                    return True
                elif not visites[i]:
                    f.enfiler(i)
                    visites[i] = True


if __name__ == "__main__":
    g = []
    
    g.append([[0, 1, 0, 1, 1, 0],
              [1, 0, 1, 0, 0, 0],
              [0, 1, 0, 1, 1, 1],
              [1, 0, 1, 0, 1, 0],
              [1, 0, 1, 1, 0, 0],
              [0, 0, 1, 0, 0, 0]])

    g.append([[0, 1, 0, 1, 0, 1, 0, 0],
              [1, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0],
              [1, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 1, 1],
              [1, 0, 1, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0]])

    for graphe in g:
        print(cycle(graphe))
        print(est_une_chaine(graphe, 0, 4))
