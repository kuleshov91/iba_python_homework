# 3	Даны три числа a, b и c. Найти среднее геометрическое этих чисел,
# если все они отличны от нуля, и среднее арифметическое в противном случае.

def geometric(nums):
    multi = 1
    for i in range(3):
        multi *= nums[i]
    print("average geometric = ", multi ** (1. / 3))

def arithmetic(nums):
    sum = 0
    for i in range(3):
        sum += nums[i]
    print("average arithmetic = ", sum / 3)

nums = []

for i in range(3):
    num = int(input("Enter a number: \n"))
    nums.append(num)

if 0 in nums:
    arithmetic(nums)
else:
    geometric(nums)

