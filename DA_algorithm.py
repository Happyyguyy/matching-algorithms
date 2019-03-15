class Agents:
    def __init__(self, name, set=None, pref=None, match=None):
        self.name = name
        self.set = set
        self.pref = pref
        self.match = match

    def __repr__(self):
        return self.name

    @property
    def pref(self):
        return self.__pref

    @pref.setter
    def pref(self, pref):
        self.pref = pref
        self.__pref = pref

    @set.setter
    def set(self, new_set):
        if (isinstance(set, SetofAgents) or set == None):
            self.set = set
        else:
            raise TypeError("Set must be of class:SetofAgents or None")
