def sortByLastDigit(inputStr):
    return inputStr[len(inputStr)-1]

i = input()
str = input().split()
str.sort(key = sortByLastDigit)
print(' '.join(str))
