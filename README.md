# GraphTheoryProjectY3S2

## Introduction
This is a program, written in Python, that uses an algorithm known as Thompson's Construction. Thompson's Construction, named after Ken Thompson, transforms the regular expression given into an equivalent Non-Deterministic Finite Automaton (NFA). This NFA then matches strings against the regular expression.

In a Deterministic Finite Automaton (DFA) you can determine the state to which the machine will move for each input symbol. However, in a Non-Deterministic Finite Automaton (NFA), the state the machine moves to cannot be determined as it can move to any combination of states in the machine. This helps to allow the user to express what they are looking for in a more easier way, as the NFA can choose between many paths.

A regular expression is a string containing several characters. Special characters can be included such as . for *concatenate*, | for *or*, * for *zero or more than one*, + for *at least one of*, ? for *zero or one of* and () for *grouping*.

## Planning
To complete this project fully and ahead of the deadline I will break this project into numerous steps, so it becomes easier to solve.
  1) Work on the Shunting Yard Algorithm which returns the infix regular expression in postfix notation
  2) Create the overall NFA which consists of several smaller NFA's of the regular expression
  3) Implement the matching algorithm which will return true if the regular expression fully matches the string
  4) Test the program to ensure that there are no bugs/faults
  5) Improve user functionality
  
## Architecture
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

## Examples
### Regular Expression's entered
1) *(a.b)*
2) *(a.b)|b**
3) *(a+b|a*)*
4) *(a?b).b**

### Test Strings entered
1) *abbb*
2) *bbbb*
3) *b*
4) *abb*

### Results
1) False
2) True
3) True
4) False

## References
Dr. Ian McLoughlin's LearnOnline Tutorials

### Thompson's Construction
https://en.wikipedia.org/wiki/Thompson%27s_construction \
https://swtch.com/~rsc/regexp/regexp1.html 

### Shunting Yard Algorithm
https://brilliant.org/wiki/shunting-yard-algorithm/ \
https://www.youtube.com/watch?v=y_snKkv0gWc

### Regular Expressions
https://www.cs.rochester.edu/u/nelson/courses/csc_173/fa/re.html \
https://www.regular-expressions.info/

### NFA
https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton \
https://people.cs.clemson.edu/~goddard/texts/theoryOfComputation/3a.pdf
