class MinStack:

    def __init__(self):
        self. arr = []
        

    def push(self, value: int) -> None:
        if len(self.arr) ==0:
            self.arr.append((value , value))
        else:
            if self.arr[-1][-1] < value:
                self.arr.append((value , self.arr[-1][-1]))
            else:
                self.arr.append((value ,value))


    def pop(self) -> None:
        if self.arr:
            self.arr.pop()

    def top(self) -> int:
        if self.arr:
            return self.arr[-1][0]

    def getMin(self) -> int:
        if self.arr:
            return self.arr[-1][-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()