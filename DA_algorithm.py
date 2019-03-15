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

    @property
    def set(self):
        return self._set

    @set.setter
    def set(self, new_set):
        if (isinstance(new_set, SetofAgents) or new_set == None):
            self._set = new_set
        else:
            raise TypeError("Set must be of class:SetofAgents or None")


class SetofAgents(set):
    def __init__(self, *args):
        if all(isinstance(each, Agent) for each in args):
            for each in args:
                each.set = self
            super().__init__(args)
        else:
            raise TypeError("args must be list of agents")
