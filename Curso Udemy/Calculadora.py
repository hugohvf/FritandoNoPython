'''
Three comments create a multiline comment
    Program: Magical Calculator
    Author: Hugo
    Coyright: 2019
'''
import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

def performMath():
    global run
    global previous
    equation = ""

    # If there has been a previous calculation, it is going to be used as prompt
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    # if user quits ->
    if equation =='quit':
        print("Goodbye, human.")
        run = False
    else:

        equation = re.sub('[a-zA-Z,.:" "]','',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()