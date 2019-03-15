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


def DA_algorithm(proposers, receivers):

    matches = set()  #set of final matches
    while proposers:
        proposals = []
        for receiver in receivers:
            proposal_set = {}
            proposal_set["receiver"] = receiver

            proposing = []
            for each in proposers:
                if each._pref[0] == receiver:
                    proposing.append(each)
            if proposing:
                proposal_set["suitors"] = proposing
                proposals.append(proposal_set)

        for proposal_set in proposals:
            # var declaration to make my life easier
            receiver = proposal_set["receiver"]
            suitors = proposal_set["suitors"]
            current_match = receiver.match


            # remove current match (if it exists from receiver) and add to list:suitors
            if current_match:
                suitors.append(current_match)    #  add to list:suitors
                receiver.match = None            #  set agent:receiver's match to None
                current_match.match = None       #  set the removed match's match to None
                proposers.add(current_match)     #  return current_match back to set of all proposers

            # closure to handle min comparison
            def return_scope(agent):
                def get_index(item):
                    return agent.pref.index(item)
                return get_index
            pref_index = return_scope(proposal_set["receiver"])

            # min comparison for best match
            best_match = min(proposal_set["suitors"], key=lambda x: pref_index(x))

            # set agent:suitors' and agent:match match to proposal_set other
            receiver.match, best_match.match = best_match, receiver

            # Remove match from set:proposers and from list:suitors
            proposers.remove(best_match)
            suitors.remove(best_match)

            # Remove preference from list of rejected suitors
            for suitor in suitors:
                removed_pref = suitor._pref.pop(0)
                #  if agent:suitor has no preference left then match with itself, remove from set:proposers, and add to return set:matches
                if (not suitor._pref) or removed_pref == suitor:
                    suitor.match = suitor
                    matches.add((suitor, suitor.match))


    for each in receivers:
        if each.match:
            matches.add((each, each.match))
        else:
            matches.add((each, each))


    return matches
