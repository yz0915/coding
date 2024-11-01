# 3. Longest Substring Without Repeating Characters: "abcabcbb" => 3 as "abc": check, add, update
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cur = set()
        ans = 0
        l = 0
        for r in range(len(s)):
            while s[r] in cur:
                cur.remove(s[l])
                l += 1
            cur.add(s[r])
            ans = max(ans, len(cur))
        return ans