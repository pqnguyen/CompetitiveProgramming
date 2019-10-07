class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, n):
        if n == 0: return []
        if n == 1: return [[1]]
        if n == 2: return [[1], [1, 1]]
        pascal = [[1], [1, 1]]
        for i in range(2, n):
            row = [1] * (len(pascal[i - 1]) + 1)
            for col in range(1, len(row) - 1):
                row[col] = pascal[i - 1][col - 1] + pascal[i - 1][col]
            pascal.append(row)
        return pascal


res = Solution().solve(1)
print(res)
