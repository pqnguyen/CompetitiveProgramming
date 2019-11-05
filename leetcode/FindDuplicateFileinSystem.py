from collections import defaultdict
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        for path in paths:
            self.transforms(path, table)
        res = []
        for ls in table.values():
            if len(ls) > 1: res.append(ls)
        return res

    def transforms(self, path, table):
        folders = path.split(" ")
        root = folders[0]
        for i in range(1, len(folders)):
            file = folders[i]
            content = ""
            filename = file
            idx = file.find("(")
            if idx != -1:
                content = file[idx:]
                filename = file[:idx]
            table[content].append(root + "/" + filename)


paths = ["root/a 1.txt(abcd) 2.txt(efsfgh)", "root/c 3.txt(abdfcd)", "root/c/d 4.txt(efggdfh)"]
print(Solution().findDuplicate(paths))
