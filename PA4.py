import null as null


def countNum(inputList):
    num = 0

    for x in range(len(inputList)):
        temp = inputList[x]
        if isinstance(temp, list):
            num += countNum(temp)
        else:
            num += 1
    return num


def palindromeRec(inputList):
    result = True
    for x in range(len(inputList)):
        temp = inputList[x]
        if isinstance(temp, list):
            result = palindromeRec(temp)

    if result == False:
        return False
    else:
        return inputList == inputList[::-1]


def palindromeIt(inputList):
    return inputList == inputList[::-1]


print("*****Problem 1*****")
try:
    temp = countNum(null)
    print(temp)
except Exception:
    print("Not a valid list!")

temp = countNum([3])
print(temp)

try:
    temp = countNum(a)
    print(temp)
except Exception:
    print("Not a valid list!")

temp = countNum([5, 1, 'a', 4])
print(temp)

temp = countNum([[1, 1, ['a']], 7, ['b', [3]]])
print(temp)

print()
print("*****Problem 2*****")

try:
    temp1 = palindromeRec(null)
    print(temp1)
    temp2 = palindromeIt(null)
    print(temp2)
except Exception:
    print("Not a valid list!")

try:
    temp1 = palindromeRec(a)
    print(temp1)
    temp2 = palindromeIt(a)
    print(temp2)
except Exception:
    print("Not a valid list!")

temp1 = palindromeRec(['a'])
print(temp1)
temp2 = palindromeIt(['a'])
print(temp2)

temp1 = palindromeRec(['a', 'b', 'c', 'b', 'a'])
print(temp1)
temp2 = palindromeIt(['a', 'b', 'c', 'b', 'a'])
print(temp2)

temp1 = palindromeRec(['a', 'b', 'c', 'c', 'b', 'a'])
print(temp1)
temp2 = palindromeIt(['a', 'b', 'c', 'c', 'b', 'a'])
print(temp2)

temp1 = palindromeRec(['a', 'b', 'c', 'a'])
print(temp1)
temp2 = palindromeIt(['a', 'b', 'c', 'a'])
print(temp2)

temp1 = palindromeRec(['a', 'b', 'd', 'e', 'f', 'f', 'c', 'b', 'd', 'a'])
print(temp1)
temp2 = palindromeIt(['a', 'b', 'd', 'e', 'f', 'f', 'c', 'b', 'd', 'a'])
print(temp2)

temp1 = palindromeRec([['a', 'b'], ['b', 'a']])
print(temp1)
temp2 = palindromeIt([['a', 'b'], ['b', 'a']])
print(temp2)
