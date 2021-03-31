class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """

        self.stack = []
        self.helpstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.helpstack) == 0 or val < self.helpstack[-1]:
            self.helpstack.append(val)
        else:
            self.helpstack.append(self.helpstack[-1])

    def pop(self) -> None:
        if len(self.stack) != 0:
            self.stack.pop(-1)
            self.helpstack.pop(-1)

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.helpstack) != 0:
            return self.helpstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()