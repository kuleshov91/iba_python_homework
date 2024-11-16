# 3	Удалить элементы, индексы которых кратны 7.

import random

numList = []
for i in range(int(input("Enter size of the list: \n"))):
    numList.append(random.randint(0,99))

print("list before deleting: ", numList)

for i in range(len(numList)):
    if i % 7 == 0 and i != 0:
        numList.pop(i)

print("list after deleting: ", numList)