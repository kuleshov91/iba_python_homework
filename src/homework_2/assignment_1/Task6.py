# Найдите сумму номеров минимального и максимального элементов.
# По целому n и n положительным целым числам определите, можно ли из них
# образовать подмножество, сумма элементов которого делится на n без остатка.
# Если можно, то найти любое из таких подмножеств.

from random import randint

numList = [randint(-5, 10) for i in range(10)]
min = numList[0]
max = -10
minIndex = 0
maxIndex = 0
indexSum = 0
positiveNums = 0

print("list at start: ", numList)

for i in range(len(numList)):
    if numList[i] > 0:
        positiveNums += 1
    if numList[i] < min:
        min = numList[i]
        minIndex = i
    if numList[i] > max:
        max = numList[i]
        maxIndex = i

indexSum = maxIndex + minIndex

print("min:", min, "index:", minIndex)
print("max:", max, "index:", maxIndex)
print("sum of indexes min and max elements: ", indexSum)

subList = []

for i in range(len(numList)):
    if numList[i] == 0:
        continue
    sum = numList[i] + positiveNums
    if sum % numList[i] == 0 or sum % positiveNums == 0:
        subList.append(numList[i])
        subList.append(positiveNums)
        break

print("sum of elements:", subList, "divided by", subList[0], "or", subList[1], "without remainder")