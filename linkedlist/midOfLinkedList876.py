# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:
    def middleNode(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow