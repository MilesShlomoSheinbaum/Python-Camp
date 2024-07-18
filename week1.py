"""sum = 0
for x in range(0, 101, 2): 
    sum += x
print (sum)
"""

"""x = 0
while x < 20:
    x += 1
    print (x)
"""


"""input = ["r", "a", "c", "e", "c", "a", "r"]
var1 = ""
var2 = ""
for x in range(0, len(input)):
    var2 += input[x]
print(var2)
for x in range( len(input) - 1, -1, -1):
    var1 += input[x]
print(var1)
if var1 == var2:
    print("True")
else:
    print("False")
"""

def isPallendrome(input):

    input = ["r", "a", "c", "e", "c", "a", "r"]
    var1 = ""
    var2 = ""
    for x in range(0, len(input)):
        var2 += input[x]
    print(var2)
    for x in range( len(input) - 1, -1, -1):
        var1 += input[x]
    print(var1)
    if var1 == var2:
        return True
    else:
        return False

answer = isPallendrome (["k", "a", "y", "a", "k"])
print("answer:", answer)