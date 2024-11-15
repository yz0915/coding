# 61. Rotate List
# https://leetcode.com/problems/rotate-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotateRight(head, k):
    if not head:
        return head

    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length += 1 

    k = k % length
    if k == 0:
        return head

    cur = head
    for i in range(length - k - 1):
        cur = cur.next

    newhead = cur.next
    cur.next = None
    tail.next = head
    return newhead