# leetcode 706
# https://leetcode.com/problems/design-hashmap/

class ListNode:
    def __init__(self, key: int, val: int, next_node=None):
        self.key = key
        self.val = val
        self.next = next_node

class MyHashMap:
    SIZE = 10000  # Constant size for the hashmap

    def __init__(self):
        self.map = [None] * self.SIZE

    def hash(self, key):
        return key % self.SIZE

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        if not self.map[index]:
            # Case 1: New key-val node
            self.map[index] = ListNode(key, value)
            return

        curr = self.map[index]
        while curr:
            if curr.key == key:
                # Case 2: Key exists, update value
                curr.val = value
                return
            if not curr.next:
                # Append a new key-value node (Case 3)
                curr.next = ListNode(key, value)
                return
            curr = curr.next

    def get(self, key: int) -> int:
        index = self.hash(key)
        curr = self.map[index]

        while curr:
            if curr.key == key:
                return curr.val  # Return value if key is found
            curr = curr.next

        return -1  # Return -1 if key is not found

        

    def remove(self, key: int) -> None:
        index = self.hash(key)
        curr = self.map[index]

        if not curr:
            # Case 1: No such key node
            return

        if curr.key == key:
            # Case 2: Top node has the key
            self.map[index] = curr.next
            return

        # Case 3: Traverse the chain to find the key
        prev = curr
        curr = curr.next

        while curr:
            if curr.key == key:
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
