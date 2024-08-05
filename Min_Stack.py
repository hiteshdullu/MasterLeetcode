class MinStack:

    def __init__(self):
        self.arr = []
        self.min_array = []

    def push(self, val: int) -> None:
        if not len(self.arr):
            self.min_array.append(val)
        else:
            last = self.min_array[-1]
            if last<val:
                self.min_array.append(last)
            else:
                self.min_array.append(val)
        self.arr.append(val)
    
    def pop(self) -> None:
        self.arr.pop()
        self.min_array.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_array[-1]
