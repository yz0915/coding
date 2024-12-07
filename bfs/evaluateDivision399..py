# lc 399
# https://leetcode.com/problems/evaluate-division/

# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# note: x is undefined => -1.0

from collections import defaultdict, deque
def calcEquation(equations, values, queries):
    adj = defaultdict(list)  # Map a -> list of [b, a/b]
    for i, eq in enumerate(equations):
        a, b = eq
        adj[a].append([b, values[i]])
        adj[b].append([a, 1 / values[i]])

    def bfs(src, target):
        if src not in adj or target not in adj:
            return -1
        
        q, visit = deque(), set() # q, visit = deque([[src, 1]]), {src}
        q.append([src, 1])
        visit.add(src)
        while q:
            n, w = q.popleft()
            if n == target:
                return w
            for nei, weight in adj[n]:
                if nei not in visit:
                    q.append([nei, w * weight])
                    visit.add(nei)
        return -1

    return [bfs(q[0], q[1]) for q in queries]