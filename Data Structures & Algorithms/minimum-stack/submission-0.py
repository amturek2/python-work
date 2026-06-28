class MinStack:
    import heapq

    def __init__(self):
        self.stack = []
        self.currMin = float('inf')
        
    def push(self, value: int) -> None:
        self.currMin = min(value, self.currMin)
        self.stack.append([value, self.currMin])

        
    def pop(self) -> None:
        tmp = self.stack[-1]
        self.stack.pop()
        if (len(self.stack)) < 1: 
            self.currMin = float('inf')
        else: 
            self.currMin = self.stack[-1][1]
        return tmp[0]

        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()