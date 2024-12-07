# lc 433
# https://leetcode.com/problems/minimum-genetic-mutation/

# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2

from collections import deque

def minMutation(startGene, endGene, bank):
    queue = deque([(startGene, 0)])
    seen = {startGene}
    
    while queue:
        node, steps = queue.popleft()
        if node == endGene:
            return steps

        for c in "ACGT":
            for i in range(len(node)):
                neighbor = node[:i] + c + node[i + 1:]
                if neighbor not in seen and neighbor in bank:
                    queue.append((neighbor, steps + 1))
                    seen.add(neighbor)

    return -1