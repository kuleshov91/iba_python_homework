# Удалить из списка все элементы, совпадающие с его минимальным значением.

import random

numList = []
for i in range(int(input("Enter size of the list: \n"))):
    numList.append(random.randint(0,99))

print("list at start:", numList)

min = numList[0]

for num in numList:
    if num < min:
        min = num

while numList.count(min) > 0:
    numList.remove(min)

print("after deleting:", numList)