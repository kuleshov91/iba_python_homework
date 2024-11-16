#4	Найти значение минимального элемента списка.

import random

numList = []
for i in range(int(input("Enter size of the list: \n"))):
    numList.append(random.randint(0,99))

print("list at start:", numList)

min = numList[0]

for num in numList:
    if num < min:
        min = num

print("min value:", min)