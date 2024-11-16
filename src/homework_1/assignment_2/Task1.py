#1 Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7.
# Могут ли два билета подряд быть удачными?

def digitSum(num):
    digitsSum = 0
    while num > 0:
        digitsSum += num % 10
        num = num // 10
    return digitsSum

for num in range(100000, 1000000):
    nextNum = num + 1
    if digitSum(num) % 7 == 0 and digitSum(nextNum) % 7 == 0:
        print("Lucky numbers: ", num, " and ", nextNum)