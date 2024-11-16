# Leetcode 2 Add Two Numbers: 2->4->3-> + 5->6->4-> = 7->0->8
# https://leetcode.com/problems/add-two-numbers/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = cur = ListNode()
    carry = 0
    while l1 or l2 or carry:
        ssum = carry
        if l1:
            ssum += l1.val
            l1 = l1.next
        if l2:
            ssum += l2.val
            l2 = l2.next
        cur.next = ListNode(ssum%10)
        carry = ssum // 10
        cur = cur.next
    return dummy.next