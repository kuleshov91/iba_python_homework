# 9	Найти среднее арифметическое элементов списка.

import random

numList = []
for i in range(int(input("Enter size of the list: \n"))):
    numList.append(random.randint(0,99))

print("list at start:", numList)

sum = 0

for num in numList:
    sum += num

print("average:", sum/len(numList))    