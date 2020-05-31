# Cracking the coding interview - 8.4
# Power Set: Write a method to return all subsets of a set.
from collections import deque


class Solution:
    def subset(self, a):
        results = [[]]
        for l in range(1, len(a) + 1):
            result = []
            self.subset_util(a, l, 0, result, [])
            results.extend(result)
        return results

    def subset_util(self, a, l, start, results, result):
        if len(result) == l:
            results.append(result[:])
            return

        for i in range(start, len(a)):
            result.append(a[i])
            self.subset_util(a, l, i + 1, results, result)
            result.pop()


class Solution1:
    def subset(self, a):
        results = self.subset_util(a, 0)
        return results

    def subset_util(self, a, index):
        if index == len(a):
            return [[]]
        results = []
        subsets = self.subset_util(a, index + 1)
        for subset in subsets:
            results.append(subset[:])
            subset.append(a[index])
            results.append(subset)
        return results


class Solution2:
    def subset(self, a):
        results = []
        m = 1 << len(a)
        for i in range(m):
            res = self.convert_bit_to_set(a, i)
            results.append(res)

        return results

    def convert_bit_to_set(self, a, n):
        res = deque()
        index = len(a) - 1
        while n:
            if n & 1:
                res.appendleft(a[index])
            index -= 1
            n = n >> 1

        return list(res)


a = [1, 2, 3, 4]

res = Solution().subset(a)
print(res)
res = Solution1().subset(a)
print(res)
res = Solution2().subset(a)
print(res)
