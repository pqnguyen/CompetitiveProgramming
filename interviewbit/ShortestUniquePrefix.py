from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.count = 0
        self.trie = {}


class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        trie = {}
        for s in A:
            self.buildtrie(trie, s)
        res = []
        for s in A:
            res.append(self.getprefix(trie, s))
        return res

    def buildtrie(self, trie, s):
        for ch in s:
            if ch not in trie:
                trie[ch] = TrieNode()
            trie[ch].count += 1
            trie = trie[ch].trie

    def getprefix(self, trie, s):
        for i, ch in enumerate(s):
            if trie[ch].count == 1: return s[:i + 1]
            trie = trie[ch].trie
        return ""


input = ["zebra", "dog", "duck", "dove"]
res = Solution().prefix(input)
print(res)
