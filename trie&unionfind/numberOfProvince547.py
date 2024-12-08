# 547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/description/

# 1 - 2
# 3
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Initialize parent array

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def unite(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        self.parent[root_y] = root_x  # Union by updating root

def findCircleNum(isConnected) :
    if not isConnected or not isConnected[0]:
        return 0
    
    n = len(isConnected)
    uf = UnionFind(n)
    unique_roots = set()
    
    # Union-Find for connected nodes
    for i in range(n):
        for j in range(i + 1, n):  # Only look at the upper triangle of the matrix
            if isConnected[i][j] == 1:
                uf.unite(i, j)
    
    # Find unique components
    for i in range(n):
        root = uf.find(i)
        unique_roots.add(root)
    
    return len(unique_roots)