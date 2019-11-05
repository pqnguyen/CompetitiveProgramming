from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        bin_reps = [format(num, "#010b")[-8:] for num in data]
        n = len(bin_reps)
        i = 0
        while i < n:
            bin_rep = bin_reps[i]
            nbytes = 0
            if bin_rep.startswith("0"): nbytes = 0
            elif bin_rep.startswith("110"): nbytes = 1
            elif bin_rep.startswith("1110"): nbytes = 2
            elif bin_rep.startswith("11110"): nbytes = 3
            else: return False

            for k in range(1, nbytes + 1):
                if i + k >= n: return False
                bin_rep = bin_reps[i + k]
                if not bin_rep.startswith("10"): return False

            i += nbytes + 1

        return i == n


data = [197, 130, 1]
res = Solution().validUtf8(data)
print(res)
