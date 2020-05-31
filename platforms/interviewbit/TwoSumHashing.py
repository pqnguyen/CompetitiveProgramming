class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        tb = {}
        for i, num in enumerate(A):
            if B - num in tb:
                return [tb[B - num] + 1, i + 1]
            if num not in tb:
                tb[num] = i
        return []


res = Solution().twoSum([2, 7, 11, 11], 22)
print(res)
