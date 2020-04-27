# Jack McNamee - G00359656
"""
    A Runner class that asks the user for a
    regular expression and a string and, if they
    match, return true
"""

from match import match

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

    # prints true or false
    print("Result is:", match(regularExpression, testString))

    # ask user if they want to continue or exit
    print("Enter any key to try again or type quit to exit: ")
    exitProgram = input()

# message for user when they are finished (entered 'quit')
print("Goodbye")
