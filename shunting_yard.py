# Jack McNamee - G00359656
# The Shunting Yard Algorithm for regular expressions

def shunting(infix):
    """ Return the infix reg expression in postfix """

    # convert the input to a stack-ish list and reverse
    infix = list(infix)[::-1]

    # operator stack
    operators = []

    # output list
    postfix = []

    # operator precedence
    prec = {'*':60, '?':50, '.':40, '|':30, ')':20, '(':10}

    # loop through the input one char at a time
    while infix:
        # pop a char from the input
        char = infix.pop()

        # decide what to do based on the char
        if char == '(':
            # push an open brack to operators[]
            operators.append(char)

        elif char == ')':
            # pop operators[] until an open bracket is found
            while opers[-1] != '(':
                postfix.append(operators.pop())
            # remove the open bracket
            operators.pop()

        elif char in prec:
            # push any operators on operators[]
            # with higher precedence to the output
            while operators and prec[char] < prec[operators[-1]]:
                postfix.append(operators.pop())
            # push char to operators[]
            operators.append(char)

        else:
            # push the char to the output(postfix)
            postfix.append(char)

    # pop all operators to the output
    while operators:
        postfix.append(operators.pop())

    # convert postfix to a string
    return ''.join(postfix)


