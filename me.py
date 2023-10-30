# Author:
# Roman Lewis
# Project:
# Numbering systems with Python


# Add appropriate header information
import sys

print("Numbering Systems with Python")
numberOfArgs = len(sys.argv)
print("Total arguments passed: " + str(numberOfArgs))
print("Argument 1: " + sys.argv[0])

# Todo: check for on arguments or more thatn two arguments and provide a meaningful error message.
if numberOfArgs == 2:
    print("Argument 2: " + sys.argv[1])
    numberAsAString = sys.argv[1]
    numberAsAnInt = int(numberAsAString, base=10)
    numberAsHex = hex(numberAsAnInt)

    print("Input: " + numberAsAString)
    print("Number: " + str(numberAsAnInt))
    print("Hex: " + numberAsHex)

print("")