# 680. Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/

'''
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:
Input: s = "aba", Output: true
'''

def validPalindrome(s):
    i, j = 0, len(s) - 1
    
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return validPalindromeUtil(s, i + 1, j) or validPalindromeUtil(s, i, j - 1)
    return True

def validPalindromeUtil(s, i, j):
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return False
    
    return True