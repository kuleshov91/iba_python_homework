nums = [5, 7, 1, 3, 9, 8, 2, 4, 6, 0]

for i in range(int(len(nums) - 1 / 2)):
    for j in range(i, len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j] = nums[j + 1]
    for j in range(len(nums) - 2 - i, i + 1):
        if nums[j] < nums[j - 1]:
            nums[j] = nums[j - 1]

print(nums)