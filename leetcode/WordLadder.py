from collections import deque, defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.cache = defaultdict(list)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        table = defaultdict(list)
        for word in wordList:
            for wordtrans in self.generateTransformation(word):
                table[wordtrans].append(word)

        visited = defaultdict(bool)
        queue = deque()
        queue.append((beginWord, 1))
        visited[beginWord] = True

        while queue:
            word, step = queue.popleft()
            if word == endWord: return step
            for wordtrans in self.generateTransformation(word):
                if wordtrans in table:
                    for originalWord in table[wordtrans]:
                        if not visited[originalWord]:
                            queue.append((originalWord, step + 1))
                            visited[originalWord] = True
        return 0

    def generateTransformation(self, word):
        if word in self.cache: return self.cache[word]
        res = []
        for i in range(len(word)):
            res.append(word[:i] + '_' + word[i + 1:])
        self.cache[word] = res
        return res


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
res = Solution().ladderLength(beginWord, endWord, wordList)
print(res)
