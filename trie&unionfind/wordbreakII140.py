# Word Break II -  Leetcode 140 - hard
# https://leetcode.com/problems/word-break-ii/

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26  # For lowercase English letters


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            index = ord(char) - ord("a")
            if not node.children[index]:
                node.children[index] = TrieNode()
            node = node.children[index]
        node.isEnd = True


class Solution:
    def wordBreak(self, s, wordDict):
        # Build the Trie from the word dictionary
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        dp = {}

        for start_idx in range(len(s), -1, -1):
            # List to store valid sentences starting from start_idx
            valid_sentences = []

            current_node = trie.root

            for end_idx in range(start_idx, len(s)):
                char = s[end_idx]
                index = ord(char) - ord("a")

                # Check if the current character exists in the trie
                if not current_node.children[index]:
                    break

                # Move to the next node in the trie
                current_node = current_node.children[index]

                # Check if we have found a valid word
                if current_node.isEnd:
                    current_word = s[start_idx : end_idx + 1]

                    # If it's the last word, add it as a valid sentence
                    if end_idx == len(s) - 1:
                        valid_sentences.append(current_word)
                    else:
                        sentences_from_next_index = dp.get(end_idx + 1, [])
                        for sentence in sentences_from_next_index:
                            valid_sentences.append(
                                current_word + " " + sentence
                            )

            dp[start_idx] = valid_sentences

        return dp.get(0, [])