# lc 1423
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

'''
Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. 
The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
'''

# Sliding Window!
def maxScore(cardPoints, k):
    l, r = 0, len(cardPoints) - k
    total = sum(cardPoints[r:])
    res = total

    while r < len(cardPoints):
        total += (cardPoints[l] - cardPoints[r])
        res = max(res, total)
        l += 1
        r += 1

    return res