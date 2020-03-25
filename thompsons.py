# Jack McNamee - G00359656
# Thompson's Construction Algorithm
# converts a regular expression into an equivalent NFA

from shunting_yard.py import shunting

class State:
    """
    A state with one or two edges, 
    all edges labelled by label
    """
    def __init__(self, edges=[], label=None):
        # every state has -1, 1 or 2 edges
        self.edges = edges
        # labels for the arrow, None means epsilon
        self.label = label
    
class Fragment:
    """ An NFA Fragment with a start state and accept state """
    def __init__(self, start_state, accept_state):
        # start state
        self.start_state = start_state
        # accept state
        self.accept_state = accept_state

def thompsons(infix):
    """ Return an NFA fragment representing the infix regular expression """

    # convert infix to postfix
    postfix = shunting(infix)
    # make postfix a stack of characters
    postfix = list(postfix)[::-1]

    # a stack for NFA fragments
    nfa_stack = []

    while postfix:
        # pop a character from postfix
        c = postfix.pop()
        if c == '.':
            # pop two fragments off the stack
            fragOne = nfa_stack.pop()
            fragTwo = nfa_stack.pop()
            
            # point fragTwo accept state at fragOne start state
            fragTwo.accept.edges.append(fragOne.start)
            # new start state is fragTwo
            start = fragTwo.start
            # new accept state is fragOne
            accept = fragOne.accept

        elif c == '|':
            # pop two fragments off the stack
            fragOne = nfa_stack.pop()
            fragTwo = nfa_stack.pop()

            # create new start and accept state
            accept = State()
            start = State(edges=[fragTwo.start, fragOne.start])
            # point the old accept states at the new one
            fragTwo.accept.edges.append(accept)
            fragOne.accept.edges.append(accept)

        elif c == '*':
            # pop a single fragment off the stack
            frag = nfa_stack.pop()

            # create new start and accept states
            accept = Start()
            start = State(edges=[frag.start, accept])

            # point the arrows
            frag.accept.edges = ([frag.start, accept])

        else:
            accept = State()
            start = State(label=c, edges=[accept])

        # create new instance of Fragment to represent the new NFA
        newFrag = Fragment(start, accept)

        # push the new NFA to the NFA stack
        nfa_stack.append(newFrag)

    return nfa_stack.pop()

# add a state to a set, and follow all of the epsilon arrows
def follows(state, current):
    # only if state has not been seen
    if state not in current:
        # put this state into current
        current.add(state)
        # if state is labelled by e(psilon)
        if state.label is None:
            # loop through states pointed to by this state
            for x in state.edges:
                # follow their e(psilon)s
                follows(x, current)






