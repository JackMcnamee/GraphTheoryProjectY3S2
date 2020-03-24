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
