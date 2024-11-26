# leetcode 1221
# https://leetcode.com/problems/split-a-string-in-balanced-strings/

def balancedStringSplit(s):
    balance = 0
    splits = 0

    for c in s:
        balance += -1 if c == 'L' else 1
        if balance == 0:
            splits += 1

    return splits