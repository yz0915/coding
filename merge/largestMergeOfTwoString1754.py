# 1754. Largest Merge Of Two Strings
# https://leetcode.com/problems/largest-merge-of-two-strings/

def largestMerge(self, word1, word2):
    res = ""
    while len(word1) != 0 and len(word2) != 0:
        if word1 > word2:  # Compare lexicographically
            res += word1[0]
            word1 = word1[1:]
        else:
            res += word2[0]
            word2 = word2[1:]
    res += word1 + word2
    return res