"""
def add(a, b):
    return a + b

y = add(3, 5)
print(y)

def sub(a, b):
    return a - b

y = sub(5, 3)
print(y)

def times(a, b):
    return a * b

y = times(3, 5)
print(y)

def divide(a, b):
    return a / b

y = divide(5, 5)
print(y)


input1 = int(input("Pick a number between 1-10 "))
input2 = int(input("Pick another number between 1-10 "))
input3 = input("Do you want to add, subtract, multiply, or divide")
if input3 == "add":
    print(input1 + input2)
elif input3 == "subtract":
    print(input1 - input2)
elif input3 == "multiply":
    print(input1 * input2)
elif input3 == "divide":
    print(input1 / input2)
"""






def challenge(inputQuestion):
    inputQuestion = input("Input a math sentence")
    return(inputQuestion)
a = challenge(12 * 5)
print(12 * 5)