# Jack McNamee - G00359656
"""
    A Runner class that asks the user for a
    regular expression and a string and, if they
    match, return true
"""

from thompsons import thompsons, follows

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
                if state.label == char:
                    # add the state at end of arrow to current
                    follows(state.edges[0], current)

    # check if NFA matches the string
    return nfa.accept in current

# welcoming message to user
print("Welcome to my Graph Theory Project")
print("Here you can check if a regular expression matches a string")

# initialize exitProgram as empty string
exitProgram = ''

while exitProgram != 'quit':
    # while loop that allows user to continue using
    # this program until they type 'quit'

    # ask user for a regular expression
    print("Please enter your regular expression here: ")
    regularExpression = input()
    
    # ask user for a string
    print("Please enter your test string here: ")
    testString = input()

    # prints true or false
    print(match(regularExpression, testString))

    # ask user if they want to continue or exit
    print("Enter 1 to try again or quit to exit: ")
    exitProgram = input()

# message for user when they are finished (entered 'quit')
print("Goodbye")
