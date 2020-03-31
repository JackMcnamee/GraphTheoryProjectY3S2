# GraphTheoryProjectY3S2

## Introduction
This is a program, written in Python, that uses an algorithm known as Thompson's Construction. Thompson's Construction, named after Ken Thompson, transforms the regular expression given into an equivalent Non-Deterministic Finite Automaton (NFA). This NFA then matches strings against the regular expression.

A regular expression is a string containing a number of characters. Special characters can be included such as . for *concatenate*, | for *or*, * for *zero or more than one*, + for *at least one of*, ? for *zero or one of* and () for *grouping*.

## Planning
To complete this project fully and ahead of the deadline I will break this project into numerous steps so it becomes easier to solve.
  1) Work on the Shunting Yard Algorithm which returns the infix regular expression in postfix notation
  2) Create the overall NFA which consists of several smaller NFA's of the regular expression
  3) Implement the matching algorithm which will return true if the regular expression fully matches the string
  4) Test the program to ensure that there are no bugs/faults
  5) Improve user functionality
