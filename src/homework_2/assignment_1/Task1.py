#Удалить в списке все числа, которые повторяются более двух раз.
#Найти подмножество данного множества чисел такое, что сумма его элементов равна заданному числу.

numList = [1, 3, 5, 6, 3, 7, 2, 6, 9, 6, 4, 8]

for num in numList:
    count = numList.count(num)
    if count >= 2:
        for i in range(count):
            numList.remove(num)

print(numList)

subList = []
enteredSum = int(input("Enter a number: \n"))
sum = 0

for num in numList:
    if num > enteredSum:
        continue
    elif num < enteredSum:
        if num + sum > enteredSum:
            continue
        elif num + sum < enteredSum:
            subList.append(num)
            sum += num
        elif num + sum == enteredSum:
            subList.append(num)
            break
    elif num == enteredSum:
        subList = [num]
        break

print(enteredSum, " is a sum of elements ", subList)