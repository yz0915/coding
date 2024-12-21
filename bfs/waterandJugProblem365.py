# lc 365
# https://leetcode.com/problems/water-and-jug-problem/

from collections import deque

def canMeasureWater(x, y, target):
    directions = [x, -x, y, -y]
    q = deque([0]) # total water in two jars
    s = set([0]) # Ensure no cycles!!
    
    while q:
        node = q.popleft()
        if node == target:
            return True
        
        for d in directions:
            n = node + d
            if n < 0 or n > x + y:
                continue
            if n not in s:
                s.add(n)
                q.append(n)
    return False