# 314. Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
from collections import deque
class Solution:
    def verticalOrder(self, root):
        if not root: return []
        columnTable = collections.defaultdict(list)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()
            columnTable[column].append(node.val)
            if node.left:
                queue.append((node.left, column - 1))
            if node.right:
                queue.append((node.right, column + 1))
                        
        return [columnTable[x] for x in sorted(columnTable.keys())]