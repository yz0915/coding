# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
            
        return prev