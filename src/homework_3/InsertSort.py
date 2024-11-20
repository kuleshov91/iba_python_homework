nums = [5, 7, 1, 3, 9, 8, 2, 4, 6]

for i in range(len(nums)):
    num = nums[i]
    j = i
    while j > 0:
        if nums[j - 1] > num:
            nums[j] = nums[j - 1]
            j -= 1
        else:
            break
    nums[j] = num

print(nums)