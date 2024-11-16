# 2	Все четные по значению элементы исходного списка A поместить в новый список B.

import random

numList = []
for i in range(int(input("Enter size of the list: \n"))):
    numList.append(random.randint(0,99))

positiveNums = []

for num in numList:
    if num % 2 == 0:
        positiveNums.append(num)

print("start list:", numList)
print("positive nums list:", positiveNums)