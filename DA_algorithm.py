class Agents:
    def __init__(self, name, group=None, pref=None, match=None):
        self.name = name
        self.group = group
        self._pref = pref
        self.match = match

    def __repr__(self):
        return self.name

    @property
    def pref(self):
        return self._pref

    @pref.setter
    def pref(self, pref):
        self._pref = pref
    
