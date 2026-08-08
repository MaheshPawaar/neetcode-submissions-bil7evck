class MinStack:
    def __init__(self):
        self.stack = []
        self.curr_min = 0

    def push(self, val: int) -> None:
        if self.stack:
            self.curr_min = min(self.stack[-1][1], val)
        else:
            self.curr_min = val
        self.stack.append((val, self.curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
