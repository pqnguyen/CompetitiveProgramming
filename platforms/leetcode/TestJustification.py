import math
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        page = []
        line = []
        length = 0
        i = 0
        while i < len(words):
            word = words[i].strip()
            isAdd = length + len(line) + len(word) <= maxWidth
            if isAdd:
                line.append(word)
                length += len(word)
                i += 1
            if not isAdd or (isAdd and i == len(words)):
                page.append(self.justifyLine(line, maxWidth, i == len(words)))
                line = []
                length = 0
        return page

    def justifyLine(self, line, maxWidth, isLastLine=False):
        length = sum(len(word) for word in line)
        if len(line) == 1 or isLastLine:
            res = " ".join(line)
            res = res + " " * (maxWidth - len(res))
            return res
        else:
            res = line[0]
            space = maxWidth - length
            i = 1
            while space:
                pad = math.ceil(space / (len(line) - i))
                res += " " * pad + line[i]
                i += 1
                space -= pad

            return res


words = ["a", "a", "a", "aaa"]
maxWidth = 6
page = Solution().fullJustify(words, maxWidth)
for line in page:
    print(line, len(line))
