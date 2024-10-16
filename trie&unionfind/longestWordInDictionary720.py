# https://leetcode.com/problems/longest-word-in-dictionary/
# Input: words = ["w","wo","wor","worl","world"]
# Output: "world"
# Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def longestWord(self, words):
        root = TrieNode()

        for word in words:
            cur = root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]
            cur.end = True
            
        res = ''
        for word in words:
            if len(word) < len(res): continue
            
            cur = root
            for letter in word:
                cur = cur.children[letter]
                if not cur.end: break
            
            if cur.end and (len(word) > len(res) or (len(word) == len(res) and word < res)):
                res = word        
            
        return res