# GraphTheoryProjectY3S2

## Introduction
This is a program, written in Python, that uses an algorithm known as Thompson's Construction. Thompson's Construction, named after Ken Thompson, transforms the regular expression given into an equivalent Non-Deterministic Finite Automaton (NFA). This NFA then matches strings against the regular expression.

In a Deterministic Finite Automaton (DFA) you can determine the state to which the machine will move for each input symbol. However, in a Non-Deterministic Finite Automaton (NFA), the state the machine moves to cannot be determined as it can move to any combination of states in the machine. This helps to allow the user to express what they are looking for in a more easier way, as the NFA can choose between many paths.

A regular expression is a string containing several characters. Special characters can be included such as . for *concatenate*, | for *or*, * for *zero or more than one*, + for *at least one of*, ? for *zero or one of* and () for *grouping*.

The files in this repository used to create the program include:
### shunting_yard.py
This python file will include the Shunting Yard algorithm. This algorithm was invented by Edsger Dijkstra and named the "Shunting Yard" algorithm because its operation resembles that of a railroad shunting yard.\
The Shunting Yard algorithm is used to parse the regular expression from infix notation to postfix notation.\
An example of this would be:\
Infix Notation: *a.b*\
Postfix Notation: *ab.*\
Converting the regular expression from infix to postfix is implemented here because the computer cannot easily distinguish between the operators and the parenthesis. This is done by creating a stack which will reverse the order of the operators of the regular expression.

### thompson.py
This file will build a series of small NFA'S which will be used to create the overall NFA, using Thompson's Construction to do so.\
The shunting algorithm created in shunting_yard.py will be imported into this file to convert the infix regular expression to postfix.\
The thompson function will then return an NFA fragment representing the infix regular expression. It will do this by splitting the regular expression into smaller expressions from which the NFA, equivalent to the regular expression, will be constructed.

### match.py
This file will implement the match algorithm which returns true if, and only if, the regular expression fully matches the string. To do so the file will import the functions created in thompson.py to compile the regular expression into an NFA. The match function will loop through the characters in the string and then check if the NFA matches the string entered by the user.\

### runner.py
This file will call the match algorithm to check if the user's regular expression and string match.\
Finally the user functionality will be implemented where the user can input a regular expression and a test string to check if the string matches the regular expression. If it does the program will return true, else it will return false. 

## How To Run Program
Install Python on your computer
```
https://www.python.org/downloads/
```
Clone this repository
```
git clone https://github.com/JackMcnamee/GraphTheoryProjectY3S2
```
Enter the directory
```
cd GraphTheoryProjectY3S2
```
Run the program
```
python3 runner.py
```

## How To Run Tests
Install Python on your computer
```
https://www.python.org/downloads/
```
Clone this repository
```
git clone https://github.com/JackMcnamee/GraphTheoryProjectY3S2
```
Enter the directory
```
cd GraphTheoryProjectY3S2
```
Run tests
```
python3 -m unittest discover -s tests
```

## Algorithms
### Shunting Yard Algorithm
The Shunting Yard algorithm is used in the program to convert the regular expression, entered by the user, from infix notation to postfix notation. This is done so the computer can more easily evaluate the regular expression.

#### How to convert from infix notation to postfix notation
We will work from left to right on the infix expression to convert it to a postfix expression
![1st step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/1.jpg)

Add the opening bracket to the operator stack as it is an operator
![2nd step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/2.jpg)

Add a to postfix as it is a character
![3rd step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/3.jpg)

Add the or operator to the operator stack
![4th step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/4.jpg)

Add b to postfix and pop everything off the operator stack as there is a closing bracket, adding the or operator to postfix
![5th step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/5.jpg)

Add the and operator to the operator stack
![6th step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/6.jpg)

Add the opening bracket to the operator stack
![7th step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/7.jpg)

Add a to postfix
![8th step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/8.jpg)

Add the kleene star to the operator stack
![9th step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/9.jpg)

As the kleene star has higher precedence, pop it off and add the or operator to the operator stack
![10th step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/10.jpg)

Add b to postfix
![11th step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/11.jpg)

Add the kleene star to the operator stack
![12th step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/12.jpg)

As there is a closing bracket, pop everything off the operator stack until you get to the opening bracket
![13th step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/13.jpg)

Finally, add the and operator to postfix
![14th step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/14.jpg)


### Thompson's Construction
This algorithm is used to convert a regular expression into an NFA.\

For a normal character x, or an empty regular expression ϵ, push the fragment to the stack
![1st step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/a.jpg)

For a . *(concatenation)*, pop two fragments from the stack and push this to the stack
![2nd step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/b.jpg)

For a | *(or)*, pop two fragments from the stack and push this to the stack
![3rd step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/c.jpg)

For a * *(kleene star)*, pop a fragment from the stack and push this to the stack
![4th step](https://github.com/JackMcnamee/GraphTheoryProjectY3S2/blob/master/Images/d.jpg)


## References
Dr. Ian McLoughlin's LearnOnline Tutorials 

### Shunting Yard Algorithm
https://brilliant.org/wiki/shunting-yard-algorithm/ \
https://www.youtube.com/watch?v=y_snKkv0gWc

### Thompson's Construction
https://en.wikipedia.org/wiki/Thompson%27s_construction \
https://swtch.com/~rsc/regexp/regexp1.html

### Regular Expressions
https://www.cs.rochester.edu/u/nelson/courses/csc_173/fa/re.html \
https://www.regular-expressions.info/

### NFA
https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton \
https://people.cs.clemson.edu/~goddard/texts/theoryOfComputation/3a.pdf

### Command Line Arguments
https://docs.python.org/3/library/argparse.html \
https://stackabuse.com/command-line-arguments-in-python/

### Testing
https://docs.python.org/3/library/unittest.html \
https://realpython.com/python-testing/

