from collections import defaultdict


class Solution:
    def countSum(self, a, target):
        count = defaultdict(int)
        count[0] = 1
        runningSum = 0
        res = 0
        for num in a:
            runningSum += num
            # if runningSum == target: res += 1
            restSum = runningSum - target
            res += count[restSum]
            count[runningSum] += 1
        return res


a = [0, 0]
res = Solution().countSum(a, 0)
print(res)
