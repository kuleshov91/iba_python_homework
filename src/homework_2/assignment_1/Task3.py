# Найдите сумму отрицательных элементов списка.
# Найдите сумму элементов списка между двумя первыми нулями. Если двух нулей нет в списке, то выведите ноль.

from random import randint

numList = [randint(-5, 5) for i in range(12)]
negativeSum = 0
sumBetweenZero = 0
index = 0

for num in numList:
    if num < 0:
        negativeSum += num

if numList.count(0) >= 2:
    index = numList.index(0)

for i in range(index + 1, len(numList)):
    if numList[i] != 0:
        sumBetweenZero += numList[i]
    else:
        break

print(numList)
print("sum of negative elements: ", negativeSum)

if numList.count(0) >= 2:
    print("sum between zero elements: ", sumBetweenZero)
else:
    print("there are not 2 zeros in the list")
