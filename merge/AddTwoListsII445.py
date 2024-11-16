# 445. Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    rl1, rl2 = reverse(l1), reverse(l2)
    dummy = cur = ListNode()
    carry = 0
    while rl1 or rl2 or carry:
        ssum = carry
        if rl1:
            ssum += rl1.val
            rl1 = rl1.next
        if rl2:
            ssum += rl2.val
            rl2 = rl2.next
        cur.next = ListNode(ssum%10)
        carry = ssum // 10
        cur = cur.next
    return reverse(dummy.next)

#          7 -> 2 -> 4 -> 3
# prev    cur nnext 
def reverse(head):
    prev, cur = None, head
    while cur:
        nnext = cur.next
        cur.next = prev
        prev = cur
        cur = nnext
    return prev