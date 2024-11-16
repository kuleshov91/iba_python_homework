#2	Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.

nums = []

for i in range(3):
    num = int(input("Enter a number: \n"))
    nums.append(num)

if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
    print("Equality met")
