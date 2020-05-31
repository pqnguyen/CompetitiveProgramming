"""
    Format a string of numbers to display a currency - example" "1234.678" to "1,234.68"
    1st approach:
    - for float, get the 2 most significant digit
    - for int, divide the number 1000 repeatedly until 0
"""


class Solution:
    def solve(self, u, l, c):
        res = [["0"] * len(c), ["0"] * len(c)]
        for i in range(len(c)):
            if c[i] == 1:
                if u > l:
                    res[0][i] = "1"
                    u -= 1
                else:
                    res[1][i] = "1"
                    l -= 1
            elif c[i] == 2:
                res[0][i] = res[1][i] = "1"
                u -= 1
                l -= 1

        if u == 0 and l == 0:
            return "".join(res[0]) + ',' + "".join(res[1])
        return "IMPOSSIBLE"


sol = Solution()
print(sol.solve(3, 2, [2, 1, 1, 0, 1]))
print(sol.solve(2, 3, [0, 0, 1, 1, 2]))
print(sol.solve(2, 2, [2, 0, 2, 0]))
