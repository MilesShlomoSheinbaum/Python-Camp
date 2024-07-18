q1 = 0
while q1 <= 10:
    print (q1)
    q1 += 1

q2 = 1
while q2 <= 50:
    print (q2)
    q2 += 1


q3_1 = 0
for q3 in range (1,51):
    q3_1 += q3
print(q3_1)

animals = ["cat", "dog", "hamster"]
print(animals)
animals.append("turtle")
del animals[0]
animals 
print(animals)


grocerylist = []
while True:
    changegrocery = input("Do you want to add to the list, remove from the list, or exit the list?")
    if changegrocery == "add":
        addgrocery = input("What do you want to add to the list?")
        grocerylist.append (addgrocery)
        print(grocerylist)

    elif changegrocery == "remove":
        removegrocery = input("what do you want to remove from the list?")
        grocerylist.remove (removegrocery)
        print(grocerylist)

    elif changegrocery == "exit":
        break