from functools import cmp_to_key
from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        a = [(*self.getLogType(log), i) for i, log in enumerate(logs)]

        def cmp(item1, item2):
            if item1[0] == item2[0] == 0:
                if item1[1] < item2[1]: return -1
                return 1
            else:
                if item1[0] == item2[0] == 1:
                    if item1[2] < item2[2]: return -1
                    return 1
                return -1 if item1[0] < item2[0] else 1

        a.sort(key=cmp_to_key(cmp))
        return [logs[i] for _, _, i in a]

    def getLogType(self, log):
        words = log.split(" ")
        for i in range(1, len(words)):
            if words[i].isnumeric():
                return 1, log
        log = " ".join(words[1:]) + " " + words[0]
        return 0, log


logs = ["1 n u", "r 527", "j 893", "6 14", "6 82"]
res = Solution().reorderLogFiles(logs)
print(res)
