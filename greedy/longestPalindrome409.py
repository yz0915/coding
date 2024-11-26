# leetcode 409
# https://leetcode.com/problems/longest-palindrome/description/

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

def longestPalindrome(s):
    odd_count = 0
    char_count = {}

    for ch in s:
        char_count[ch] = char_count.get(ch, 0) + 1
        if char_count[ch] % 2 == 1:
            odd_count += 1
        else:
            odd_count -= 1

    if odd_count > 1:
        return len(s) - odd_count + 1
    return len(s)