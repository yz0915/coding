# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [0] * k
        self.head = 0
        self.count = 0 

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        # Calculate the index for the new value and insert it
        index = (self.head + self.count) % self.size
        self.queue[index] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        # Move the head to the next position
        self.head = (self.head + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        # Calculate the rear index
        rear_index = (self.head + self.count - 1) % self.size
        return self.queue[rear_index]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size