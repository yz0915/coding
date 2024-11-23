# https://leetcode.com/problems/flatten-2d-vector/

class Vector2D:

    def __init__(self, vec):
        self.data = vec
        self.outer_index = 0
        self.inner_index = 0

    def next(self) -> int:
        if self.hasNext():
            val = self.data[self.outer_index][self.inner_index]
            self.inner_index += 1
            return val

    def hasNext(self) -> bool:
        while self.outer_index < len(self.data):
            if self.inner_index < len(self.data[self.outer_index]):
                return True
            self.outer_index += 1
            self.inner_index = 0
        return False