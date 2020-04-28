# Jack McNamee - G00359656
"""
    A Runner class that asks the user for a
    regular expression and a string and, if they
    match, return true
"""

import argparse

from match import match

# program description
helpText = ( "This is a program to check if a regular expression "
       "matches a string.\n First, you enter a "
       "regular expression, then a string.\n The program will "
       "return true if they match, or false if otherwise.")

# initiate parser with description
parser = argparse.ArgumentParser(description=helpText)

# add verbose command line argument
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

# reads arguments from the command line
args = parser.parse_args()

# let user know they selected the verbosity option
if args.verbose:
    print ("Verbosity turned on")

#welcoming message to user
print("Welcome to my Graph Theory Project - Jack McNamee")
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
    
    result = match(regularExpression, testString)

    # if verbosity selected and result is true
    if args.verbose and result == 1:
        print("The regular expression and string you entered match!")
    
    # if verbosity selected and result is false
    elif args.verbose:
        print("The regular expression and string you entered do not match")

    # if verbosity is not selected    
    else:
        # prints true or false
        print("Result is:", match(regularExpression, testString))

    # ask user if they want to continue or exit
    print("Enter any key to try again or type quit to exit: ")
    exitProgram = input()

# message for user when they are finished (entered 'quit')
print("Goodbye")
