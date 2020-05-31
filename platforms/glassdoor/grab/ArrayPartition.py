class Solution:
    def solution(self, a):
        min_a, max_a = a[:], a[:]
        for i in range(1, len(a)):
            max_a[i] = max(a[i], max_a[i - 1])

        for i in range(len(a) - 2, -1, -1):
            min_a[i] = min(a[i], min_a[i + 1])

        res = len(a)
        for i in range(len(a) - 1):
            if max_a[i] < min_a[i + 1]:
                res = i + 1
                break
        return res


sol = Solution()
# 3
print(sol.solution([5, -2, 3, 8, 6]))
# 4
print(sol.solution([-5, -5, -5, -42, 6, 12]))
# 4
print(sol.solution([5, -2, 3, -1, 6]))
# 1
print(sol.solution([1, 2, 3, 4, 5, 6]))
# 2
print(sol.solution([1, 1]))
