# Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
# Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.

from random import randint

numList = [randint(0, 5) for i in range(10)]
min = numList[0]

print("list before sorting: ", numList)

for i in range(len(numList)):
    if numList[i] < min and i % 2 == 0:
        min = numList[i]
    if numList[i] == 0:
        numList.insert(0, numList.pop(i))

print("min even number: ", min)
print("list after sorting: ", numList)
