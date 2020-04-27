# Jack McNamee - G00359656
"""
    A class that compares a regex 
    and a string
"""

from thompsons import thompsons, follows

def match(regex, s):
    # returns true if the regular expression
    # and string are equal

    # compile the regular expressions into an NFA
    nfa = thompsons(regex)

    # try to match the regular expression into an NFA
    # current set of states
    current = set()
    follows(nfa.start, current)

    # previous set of states
    previous = set()

    # loop through characters in the string
    for char in s:
        # keeping track of where we were
        previous = current
        # create a new empty set for states
        current = set()
        # loop through the previous states
        for state in previous:
            # only follow arrows not labelled by s
            if state.label == char:
                # add the state at end of arrow to current
                follows(state.edges[0], current)

    # check if NFA matches the string
    return nfa.accept in current
