# New calculator

def addingNumbers(noOne, noTwo):
    print(f"{noOne} + {noTwo} equals {noOne + noTwo}")

def subtractingNumbers(noOne, noTwo):
    subtractionSum = noOne - noTwo

    if subtractionSum < 0:
        print("Answer is a negative number")
    else:
        print(f"{noOne} - {noTwo} equals {subtractionSum}")

def multiplyingNumbers(noOne, noTwo):
    print(f"{noOne} times {noTwo} equals {noOne * noTwo}")

def dividingNumbers(noOne, noTwo):
    print(f"{noOne} divided by {noTwo} equals {noOne / noTwo}")