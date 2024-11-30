# 821. Shortest Distance to a Character
# https://leetcode.com/problems/shortest-distance-to-a-character/

'''
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
'''
def shortestToChar(s, c):
    pos = -len(s)  # Initialize to a large negative value
    res = [0] * len(s)

    # Left to right pass
    for i in range(len(s)):
        if s[i] == c:
            pos = i
        res[i] = i - pos

    # Right to left pass
    pos = 2 * len(s)  # Initialize to a large positive value
    for i in range(len(s) - 1, -1, -1):
        if s[i] == c:
            pos = i
        res[i] = min(res[i], pos - i)

    return res