# 109. Convert Sorted List to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(self, head):
    # 1. Base case
    if not head:
        return None
    if not head.next:
        return TreeNode(val=head.val)

    # 2. Find the middle node to use as root
    pre, slow, fast = None, head, head
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next

    # Disconnect left half from the middle
    if pre:
        pre.next = None

    root = TreeNode(val = slow.val)

    root.left = sortedListToBST(head)
    root.right = sortedListToBST(slow.next)

    return root