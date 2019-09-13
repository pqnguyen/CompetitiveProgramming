# 1086 - High Five
from collections import defaultdict

TOP_MAX = 5


class Solution:
    def highFive(self, scores):
        studentInfo = defaultdict(list)
        for sid, score in scores:
            topFive = studentInfo[sid]
            if len(topFive) < TOP_MAX:
                topFive.append(score)
            else:
                minIndex = topFive.index(min(topFive))
                if score > topFive[minIndex]:
                    topFive[minIndex] = score

        res = []
        sortedIds = sorted(studentInfo.keys())
        for sid in sortedIds:
            topFive = studentInfo[sid]
            averageScore = sum(topFive) // 5
            res.append([sid, averageScore])
        return res


scores = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
res = Solution().highFive(scores)
print(res)
