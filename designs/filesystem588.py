# 588. Design In-Memory File System
# https://leetcode.com/problems/design-in-memory-file-system

import collections

class TrieNode:
    def __init__(self):
        self.content = ""
        self.children = collections.defaultdict(TrieNode)
        self.isfile = False
    

class FileSystem:
    def __init__(self):
        self.top = TrieNode()

    def ls(self, path):
        path_lst = path.split("/")
        node = self.top
        for p in path_lst:
            if not p:
                continue
            node = node.children.get(p)
        if node.isfile:
            return [p]
        ans = [i for i in node.children.keys()]
        if not ans:
            return ans
        ans.sort()
        return ans
        
        
    def mkdir(self, path):
        path_lst = path.split("/")
        node = self.top
        for p in path_lst:
            if not p:
                continue
            node = node.children[p]

    def addContentToFile(self, filePath, content):
        path_lst = filePath.split("/")
        node = self.top
        for p in path_lst:
            if not p:
                continue
            node = node.children[p]
        node.content += content
        node.isfile = True
    
    def readContentFromFile(self, filePath):
        path_lst = filePath.split("/")
        node = self.top
        for p in path_lst:
            if not p:
                continue
            node = node.children.get(p)
        return node.content
        