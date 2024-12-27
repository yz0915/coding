# lc 1530
# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/

'''
     1
   /   \
  2     3
 / \   /  \
4   5 6    7

Input: root = [1,2,3,4,5,6,7], distance = 3
Output: 2
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countPairs(self, root, distance):
        self.pairs = 0

        def dfs(node):
            # BASE CASE!!!
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left_dist = dfs(node.left)
            right_dist = dfs(node.right)
            
            for d1 in left_dist:
                for d2 in right_dist:
                    if d1 + d2 <= distance:
                        self.pairs += 1
            
            all_dist = left_dist + right_dist
            return [d + 1 for d in all_dist]

        dfs(root)
        return self.pairs