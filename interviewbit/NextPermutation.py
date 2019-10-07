class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, a):
        n = len(a)
        if n == 1: return a
        i = n - 2
        while i >= 0 and a[i] >= a[i + 1]: i -= 1
        if i < 0: return self.reverse(a, 0, n - 1)
        j = n - 1
        while j > i and a[i] >= a[j]: j -= 1
        a[i], a[j] = a[j], a[i]
        self.reverse(a, i + 1, n - 1)
        return a

    def reverse(self, a, i, j):
        while i < j:
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        return a


res = Solution().nextPermutation([5, 1, 1])
print(res)
