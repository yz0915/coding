# 19. Remove kth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# dummy->1->2->3->4->5->nil
#  l           r
#              l         r

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(self, head, n):
    dummy = left = ListNode(0, head)
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next