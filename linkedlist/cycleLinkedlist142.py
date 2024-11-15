# 142. Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/

def detectCycle(self, head):
        visited = set()
        start = head

        while start:
            if start in visited:
                return start
            visited.add(start)
            start = start.next

        return None