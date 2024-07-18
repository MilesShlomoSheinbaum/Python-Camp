practicelist = ["United States", "Canada", "China"]

for country in practicelist:
    print(country)

list1 = []
for numbers in range (1,11):
    list1.append(numbers)
print(list1)


list2 = []
for numbers2 in range (1,51):
    list2.append(numbers2)
print(list2)


practice = 1
while practice < 11:
    print(practice)
    practice+=1

y = 2
while y <= 20:
    print (y)
    y += 2 


    Fruit = ["apple","pear","orange","grape"]
print (Fruit)
removeFruit = input("What fruit do you want to remove from the list?")
Fruit.remove(removeFruit)
addFruit = input("What fruit do you want to add?")
Fruit.append(addFruit)
print(Fruit)