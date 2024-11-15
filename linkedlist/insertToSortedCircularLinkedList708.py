# 708. Insert into a Sorted Circular Linked List: 1. empty, 2. regular, 3. all the sames
# https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

# Input: head = [3,4,1], insertVal = 2
# Output: [3,4,1,2]

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def insert(head, insertVal):
    # 1. Empty list
    if not head:
        newNode = Node(insertVal)
        newNode.next = newNode  # Point to itself
        return newNode

    # 2. Two-zone
    curr = head.next
    while curr != head:
        if curr.val <= insertVal <= curr.next.val:
            insert_after(curr, insertVal)
            return head
        if curr.val > curr.next.val:  # End-beginning case
            if insertVal >= curr.val or insertVal <= curr.next.val:
                insert_after(curr, insertVal)
                return head
        curr = curr.next

    # 3. all elements in the circular linked list are the same
    insert_after(curr, insertVal)
    return head

def insert_after(curr, x):
    new_node = Node(x)
    new_node.next = curr.next
    curr.next = new_node