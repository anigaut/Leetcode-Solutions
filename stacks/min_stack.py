# Need to maintain the minimum value to ensure that its retrieval can happen in O(1) time
# Maintain another stack that tracks the minimum when a new number is pushed to the main stack

class MinStack:
    def __init__(self):
       self.stack = []
       self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]