# 10	Найти среднее арифметическое трех последних элементов списка.

import random

numList = []
for i in range(int(input("Enter size of the list: \n"))):
    numList.append(random.randint(0,99))

print("list at start:", numList)

sum = 0

for i in range(len(numList) - 1, len(numList) - 4, -1):
    sum += numList[i]

print("average of three last values:", sum / 3)