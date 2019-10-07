class Solution:
    # @param A : integer
    # @return a list of list of integers
    def solve(self, n):
        if n == 0: return [1]
        if n == 1: return [1, 1]
        prev_row = [1, 1]
        for i in range(1, n):
            row = [1] * (len(prev_row) + 1)
            for col in range(1, len(row) - 1):
                row[col] = prev_row[col - 1] + prev_row[col]
            prev_row = row
        return prev_row


res = Solution().solve(2)
print(res)
