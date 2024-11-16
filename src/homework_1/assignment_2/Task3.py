# . О каждом учащемся класса известны его пол, год рождения, рост и вес.
# Определить, сколько в классе мальчиков и сколько девочек. Найти средний возраст мальчиков и девочек.
# Определить, верно ли, что самый высокий мальчик весит больше всех в классе,
# а самая маленькая девочка является самой юной среди девочек.

import sys
from datetime import datetime

studentAmount = int(input("Enter student amount: "))
sex = []
yearOfBirth = []
height = []
weight = []

for i in range(studentAmount):
    sex.append(input(f"Enter sex of student {i + 1} (m, f): "))
    yearOfBirth.append(int(input(f"Enter year of birth of student {i + 1}: ")))
    height.append(int(input(f"Enter height of student {i + 1}: ")))
    weight.append(int(input(f"Enter weight of student {i + 1}: ")))
    print("")

currentYear = datetime.now().year
maleCount = 0
femaleCount = 0
maleAgeSum = 0
femaleAgeSum = 0
maxHeight = 0
highestBoy = 0
minHeight = sys.maxsize
shortestGirl = 0
fattestStudent = 0
youngestGirl = 0

for i in range(studentAmount):
    if fattestStudent < weight[i]:
        fattestStudent = weight[i]
    if sex[i] == "m":
        if maxHeight < height[i]:
            maxHeight = height[i]
            highestBoy = i
        maleCount += 1
        maleAgeSum += currentYear - yearOfBirth[i]
    if sex[i] == "f":
        if minHeight > height[i]:
            minHeight = height[i]
            shortestGirl = i
        if youngestGirl < yearOfBirth[i]:
            youngestGirl = yearOfBirth[i]
        femaleCount += 1
        femaleAgeSum += currentYear - yearOfBirth[i]

isFattest = False
isYoungest = False

if weight[highestBoy] >= fattestStudent:
    isFattest = True
if yearOfBirth[shortestGirl] >= youngestGirl:
    isYoungest = True

print("--------------------------------------------------------------")
print(f"There are {maleCount} boys")
print(f"There are {femaleCount} girls")
print("Average age of boys: ", round(maleAgeSum / maleCount, 2))
print("Average age of girls: ", round(femaleAgeSum / femaleCount, 2))
print(f"The highest boy is {"fattest in the class" if isFattest else "not fattest"}")
print(f"The shortest girl is {"youngest in the class" if isYoungest else "not youngest"}")

