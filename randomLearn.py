#import random
#list = []
#for x in range (1, 10):
#    randomNumber = random.randint(1, 10)
#    list.append(randomNumber)
#print(list)



import random
number = random.randint(1, 100)

while True:
    guess = int(input("I picked a number from one to one hundred, you need to try to guess it. What is your first guess?"))
    if guess == number:
        print ("Good job!")
        break
    elif guess < number:
        print ("Too low, guess higher!")
    elif guess > number:
        print("Too high, guess lower!")