# lc 637
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

'''
        3
       /  \
      9    20
    /   \
   15    7
    
Input: root = [3,9,20,15,7]
Output: [3.00000,14.50000,11.00000]
'''
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def averageOfLevels(root):
        res = []
        queue = deque([root])
        while queue:
            level_sum = 0
            level_count = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                level_sum += node.val
                level_count += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level_sum / level_count)
        return res