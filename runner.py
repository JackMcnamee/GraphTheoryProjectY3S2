# Jack McNamee - G00359656
"""
    A Runner class that asks the user for a
    regular expression and a string and, if they
    match, return true
"""

import thompsons

def match(regex, s):
    # returns true if the regular expression 
    # and string entered by the user are equal

    # compile the regular expressions into an NFA
    nfa = thompsons(regex)

    # try to match the regular expression to the string
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
            if state.label is not None:
                # if the label of the state is equal to the char
                if state.label == c:
                    # add the state at end of arrow to current
                    follows(state.edges[0], current)

    # check if NFA matches the string
    return nfa.accept in current

print(match("a.b|b*", "bbbb"))

