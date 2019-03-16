class Agent:
    def __init__(self, name, set=None, pref=None, match=None):
        self.name = name
        self.set = set
        self.__pref = pref
        self._pref = pref
        self.match = match

    def __repr__(self):
        return self.name

    @property
    def pref(self):
        return self.__pref

    @pref.setter
    def pref(self, pref):
        self._pref = pref
        self.__pref = pref

    def reset(self):
        self._pref == self.__pref

class SetofAgents(set):
    def __init__(self, *args):
        if all(isinstance(each, Agent) for each in args):
            for each in args:
                each.set = self
            super().__init__(args)
        else:
            raise TypeError("args must be list of agents")


def TTC_algorithm(paired_set):
    # create matrix from paired_set
    pairing_matrix = [[x[i] for x in paired_set] for i in (0,1)]

    # return set
    return_set = set()

    # initial pointing and remove cycles of length 1
    i = 0
    while 1:
        tenant, endowment = pairing_matrix[0][i], pairing_matrix[1][i]

        # pointing
        endowment.pointer, tenant.pointer = tenant, tenant._pref[0]

        # pair and remove cycles of length 1
        if tenant.pointer == endowment:
            return_set.add((pairing_matrix[0].pop(i), pairing_matrix[1].pop(i)))
            i -= 1

        if i == len(pairing_matrix[0]) - 1:
            break
        else:
            i += 1

    
    return return_set
