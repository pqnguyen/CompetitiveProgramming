class Solution:
    # @param A : integer
    # @return a list of list of integers
    def prettyPrint(self, A):
        n = A * 2 - 1
        a = [[1] * n for _ in range(n)]
        for layer in range(n // 2):
            for i in range(layer, n - layer):
                a[layer][i] = A
                a[n - layer - 1][i] = A
            for i in range(layer + 1, n - layer - 1):
                a[i][layer] = A
                a[i][n - layer - 1] = A
            A -= 1
        return a


res = Solution().prettyPrint(2)
for row in res:
    print(row)
