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


