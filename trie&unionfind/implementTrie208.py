# Implement Trie (Prefix Tree) - hard
# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                curr.children[i] = TrieNode()

            curr = curr.children[i]
        curr.isWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for c in word:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False
    
            curr = curr.children[i]
        return curr.isWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            i = ord(c) - ord("a")
            if curr.children[i] == None:
                return False

            curr = curr.children[i]
        return True