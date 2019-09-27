from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        indices = {}
        for i in range(len(S)): indices[S[i]] = i
        startIndex, destIndex = 0, -1
        res = []
        for i in range(len(S)):
            destIndex = max(destIndex, indices[S[i]])
            if i == destIndex:
                if res:
                    res.append(destIndex - startIndex + 1)
                else:
                    res.append(destIndex + 1)
                startIndex = i + 1
        return res


res = Solution().partitionLabels("abcde")
print(res)
