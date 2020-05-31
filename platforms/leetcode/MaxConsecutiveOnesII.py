class Solution:
    def maxConsecutiveOnes(self, a):
        right = [0] * (len(a) + 1)
        consecutive = 0
        for i in range(len(a) - 1, -1, -1):
            if a[i] == 1:
                consecutive += 1
            else:
                consecutive = 0
            right[i] = consecutive

        res = consecutive = 0
        for i in range(len(a)):
            if a[i] == 1:
                consecutive += 1
            else:
                res = max(res, consecutive + 1 + right[i + 1])
                consecutive = 0
                res = max(res, consecutive)
        return res


res = Solution().maxConsecutiveOnes([])
print(res)
