class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, A, B):
        a = [i for i in range(1, A + 1)]
        return self.getPermutationHelper(a, B - 1)

    def getPermutationHelper(self, a, k):
        if not a: return ""
        f = self.factorial(len(a) - 1)
        pos = k // f
        k = k % f
        ch = str(a.pop(pos))
        return ch + self.getPermutationHelper(a, k)

    def factorial(self, n):
        res = 1
        for i in range(1, n + 1): res *= i
        return res


res = Solution().getPermutation(3, 4)
print(res)
