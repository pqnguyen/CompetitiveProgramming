from typing import List


class TrieNode:
    def __init__(self):
        self.isWord = False
        self.word = ""
        self.children = {}

    def insert(self, word):
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isWord = True
        node.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        trie = TrieNode()
        for word in words: trie.insert(word)
        res = set()
        for i in range(m):
            for j in range(n):
                ch = board[i][j]
                if ch in trie.children:
                    self.findWordsHelper(board, m, n, i, j, set(), trie.children[ch], res)
        return list(res)

    def findWordsHelper(self, board, m, n, row, col, visited, trie, res):
        visited.add((row, col))
        if trie.isWord:
            res.add(trie.word)

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r = dr + row
            c = dc + col
            if 0 <= r < m and 0 <= c < n and (r, c) not in visited:
                ch = board[r][c]
                if ch in trie.children:
                    nextNode = trie.children[ch]
                    self.findWordsHelper(board, m, n, r, c, visited, nextNode, res)
        visited.remove((row, col))


board = [["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]]
words = ["oath", "pea", "eat", "rain"]
res = Solution().findWords(board, words)
print(res)
