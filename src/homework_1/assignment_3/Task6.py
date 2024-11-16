# 6	Удалить все элементы с заданным значением, если они имеются в списке.

import random

numList = []
for i in range(int(input("Enter size of the list: \n"))):
    numList.append(random.randint(0,99))

print("list at start:", numList)

num = int(input("Enter the number you want to delete: \n"))

while numList.count(num) > 0:
    numList.remove(num)

print("after deleting:", numList)