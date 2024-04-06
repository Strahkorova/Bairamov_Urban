
class EvenNumbers:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end
        if self.start == None:
            self.start = 0
        if self.end == None:
            self.end = 1
        if self.start > self.end:
            print(f"Значение start = {self.start} больше, чем значение end = {self.end}. Это не допустимо!")

    def __iter__(self):
        self.start = self.start - 1
        return self

    def __next__(self):
        self.start += 1
        if self.start <= self.end:
            if self.start % 2 == 0:
                return self.start
        else:
            raise StopIteration()


for i in EvenNumbers(10, 125):
    if i != None:
        print(i)
    else:
        pass
