class Tribonacci:

    nums = []

    def __init__(self, size):
        self.index = 0
        self.size = size

    def __next__(self):
        self.index += 1
        if self.index > self.size:
            raise StopIteration
        if self.index == 1 or self.index == 2 or self.index == 3:
            self.nums.append(1)
        if self.index >= 4:
            num = self.nums[self.index - 2] + self.nums[self.index - 3] + self.nums[self.index - 4]
            self.nums.append(num)
        return self.nums[self.index - 1]

    def __iter__(self):
        return self

itr = Tribonacci(35)
for x in itr:
    print(x)