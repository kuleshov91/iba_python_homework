# 5	Для каждого четного по номеру элемента списка A найти его сумму
# со следующим элементом и записать эти суммы в новый список B.

import random

numList = []
for i in range(int(input("Enter size of the list: \n"))):
    numList.append(random.randint(0,99))

print("list at start:", numList)

newList = []

for i in range(len(numList) - 1):
    if i % 2 == 0:
        newList.append(numList[i] + numList[i + 1])

print("new list:", newList)        