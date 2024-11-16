# 8	Найти значение максимального элемента списка.

import random

numList = []
for i in range(int(input("Enter size of the list: \n"))):
    numList.append(random.randint(0,99))

print("list at start:", numList)

max = 0

for num in numList:
    if num > max:
        max = num

print("max value: ", max)        