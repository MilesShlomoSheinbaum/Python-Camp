ice_cream = input("Would you like vanila, or chocolate ice cream?")
if ice_cream == "Vanila" or ice_cream == "vanila":
    print("Vanila ice cream is 1$")
elif ice_cream == "Chocolate" or ice_cream == "chocolate":
    print("Chocolate ice cream is 1.50$")
else:
    print("That is not a valid response")


animals = ["bear", "fish", "dog", "cat"]
print(animals)
add_animals = input("What animal do you want to add to the list?")
animals.append(add_animals)
print(animals)
del_animals = input("Which animal do you want to delete from the list?")
animals.remove (del_animals)
print (animals)