class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, A):
        res = val = 0
        for num in A:
            if val ^ num == 0:
                res += 1
                val = 1 - val
        return res


res = Solution().bulbs([0, 1, 0, 0, 0])
print(res)
