# 1381. Design a Stack With Increment Operation
# https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = [0] * maxSize
        self.maxSize = maxSize
        self.top = -1  # Top points to the last added element; -1 means the stack is empty

    def push(self, x: int) -> None:
        if self.top + 1 < self.maxSize:  # Check if there's space to add an element
            self.top += 1
            self.stack[self.top] = x

    def pop(self) -> int:
        if self.top < 0:  # Stack is empty
            return -1
        x = self.stack[self.top]
        self.top -= 1
        return x

    def increment(self, k: int, val: int) -> None:
        count = self.top + 1  # Number of elements currently in the stack
        count = min(count, k)  # Increment only up to the first k elements
        for i in range(count):
            self.stack[i] += val