# Roll-Dice
This is a simple project of an algorithm that rolls D&D dice with modifiers at a command prompt.

### Purpose
This project was developed to study the use of **Regex** in identifying patterns in user input collection routines, this being the main function that allows receiving a command input in a single line and returning appropriate behavior from the code.

### Info
Files: 2
Classes: 1
External Libraries: re, os, random and functools
Functions: 5
Lines: 89

## Operation
The code was built in PyCharm and works with it's terminal, however, it is best to run in a separate command prompt. There are four commands that the user can use: 'roll', 'set', 'clear' and 'quit'.

### Rolling Dice

#### Collection Routine
The first and main 'roll' command accepts a series of parameters, by default limited to just 2 digits, to allow dice rolls in the following format: 99d100+99-99
To validate the format used, the algorithm uses a **Regex pattern** to scan the string that the user offers as input. The first parameter is the amount of dice to be rolled, followed by the dice type limited by an internal variable that only allows the dice types: d100, d50, d20, d12, d10, d8, d6, d4, d3 and d2. The third parameter is the modifiers, they are collected in the order: positive_modifier, negative_modifier; If the algorithm does not find them in that order, it will only collect what respects the order, for example:
roll 1d20-4+2
For the modifiers parameter, it will only collect the ['-4'] value and not the full ['-4', +2']

#### Rolling Dice
To roll dices the algorithm uses a simple **randint** from Python's random library to generate pseudo-random numbers and stores them in a list, after which the values are added with the high-order function **reduce** from functools library. Modifiers are stored in an secondary list, if the user passed a value to them, the list will also be added with the **reduce** function and will have a final value to be added to the rolled dices.

### Defining Test Difficulty Class

#### Collection Routine
Check for Difficulty Class (DC) is a concept in many tabletop role-playing games, not exclusive to D&D, where a value is defined and a _success_ is possible only when the value rolled on the dice is greater than the DC of the test. The 'set' command also uses a **Regex pattern** to collect the user input, which is limited to two digits equal to the parameters of the 'roll' command.

#### Passing Tests
Initially the DC is set to None, but if the user modifies this parameter, the algorithm will always compare a new roll to the defined DC value, returning to the user whether he passed the test or not.

### Other Commands
The 'clear' command is useful for clearing the prompt screen whenever the user wants, preserving only the print with the command instructions, while the 'quit' command is used to exit the loop and stop code execution
