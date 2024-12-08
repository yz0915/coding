# lc 684
# https://leetcode.com/problems/redundant-connection/

# 1 - 2
# | /
# 3
# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Initialize parent array
        self.rank = [0] * size 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False  # x and y are already connected (cycle detected)
        
        # Union by rank
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True

def findRedundantConnection(edges):
    n = len(edges)
    uf = UnionFind(n + 1)  # Nodes are 1-indexed, so we use size n + 1

    for u, v in edges:
        if not uf.union(u, v):  # If union returns False, a cycle is detected
            return [u, v]