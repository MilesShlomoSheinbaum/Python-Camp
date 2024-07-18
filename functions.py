import random
def roll_dice():
    roll = random.randint(1,6)
    return roll

x = roll_dice()
print(x)



def addOne(number):
    return number + 1


x = addOne(4)
print(x)

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