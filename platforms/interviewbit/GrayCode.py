class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, n):
        res = ['0', '1']
        i = 2
        while i < 2 ** n:
            res.extend(list(reversed(res[:])))
            for j in range(i): res[j] = '0' + res[j]
            for j in range(i, i * 2): res[j] = '1' + res[j]
            i = i * 2
        return [self.binaryTodecimal(binary) for binary in res]

    def binaryTodecimal(self, s):
        res = 0
        for i in range(len(s)):
            res = res << 1 | int(s[i])
        return res


res = Solution().grayCode(2)
print(res)
