class Tribonacci:
    def __init__(self, size):
        self.index = 0
        self.a, self.b, self.c = 1, 1, 1
        self.size = size

    def __next__(self):
        self.index += 1
        if self.index > self.size:
            raise StopIteration
        if self.index == 1 or self.index == 2 or self.index == 3:
            return 1
        if self.index >= 4:
            result = self.a + self.b + self.c
            self.a, self.b, self.c = self.b, self.c, result
            return result

    def __iter__(self):
        return self

itr = Tribonacci(35)
for x in itr:
    print(x)