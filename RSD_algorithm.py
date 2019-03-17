from random import shuffle

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


def RSD_algorithm(tenants, houses):
    # randomize tenants
    shuffle(tenants)
    # return set
    matched_set = set()

    for tenant in tenants:
        for pref in tenant.pref:
            if pref in houses:
                matched_set.add((tenant, pref))
                break

    return matched_set
