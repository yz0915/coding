# 146. LRU cache
# https://leetcode.com/problems/lru-cache/

# ordered_dict.move_to_end('b') # Moves 'b' to the end
# ordered_dict.move_to_end('c', last=False)  # Moves 'c' to the front

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move the key to the end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            self.cache[key] = value
            if len(self.cache) > self.capacity:
                # Remove the least recently used item (first item)
                self.cache.popitem(last=False)