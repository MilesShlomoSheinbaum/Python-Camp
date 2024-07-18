
"""
def checkEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(checkEven(8560))

var = checkEven(346)
print(var)
"""






def practice(number, number2):
    print(number ** number2)

practice(2,10)

def practice2(hours, mins, secs):
    hourstosecs = hours * 60 * 60
    mintosecs = mins * 60
    return (hourstosecs + mintosecs + secs)

a = practice2(3, 20, 50)
print(a)


def getaverage(nums):
    totalSum = 0
    for x in range(0, len(nums)):
        totalSum += nums[x]
    avg = totalSum / len(nums)
    return avg
print(getaverage([1, 2, 3, 4, 5]))

