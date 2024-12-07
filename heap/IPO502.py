# lc 502
# https://leetcode.com/problems/ipo/

# Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
# Output: 4
# Explanation: Since your initial capital is 0, you can only start the project indexed 0.
# After finishing it you will obtain profit 1 and your capital becomes 1.
# With capital 1, you can either start the project indexed 1 or the project indexed 2.
# Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
# Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.

# two heap problem
import heapq


def findMaximizedCapital(k, w, profits, capital):
    # O(nlogn)
    maxProfit = [] # only projects we can afford
    minCapital = [(c, p) for c, p in zip(capital, profits)]
    heapq.heapify(minCapital)

    for i in range(k):
        
        while minCapital and minCapital[0][0] <= w:
            c, p = heapq.heappop(minCapital)
            heapq.heappush(maxProfit, -1 * p)
        if not maxProfit:
            break
        w += -1 * heapq.heappop(maxProfit)
    return w