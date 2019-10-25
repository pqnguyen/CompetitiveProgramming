from collections import Counter


class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        counter = Counter(A)
        dp = {}
        res = 0
        for num in A:
            if num not in dp:
                res = max(res, self.longestConsecutiveHelper(num, dp, counter))
        return res

    def longestConsecutiveHelper(self, ele, dp, counter):
        res = 0
        num = ele
        while num in counter:
            if num in dp:
                res += dp[num]
                break
            res += 1
            dp[num] = 1
            num = num - 1
        dp[ele] = res
        return res


res = Solution().longestConsecutive([1, 2, 3, 5, 7])
print(res)
