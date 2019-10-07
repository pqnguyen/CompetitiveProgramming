from functools import cmp_to_key


class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = [str(ele) for ele in A]
        A.sort(key=cmp_to_key(self.cmp))
        left = 0
        while A[left] == '0' and left < len(A) - 1: left += 1
        return "".join(A[left:])

    def cmp(self, a, b):
        return -1 if a + b > b + a else 1


res = Solution().largestNumber([0, 0, 0])
print(res)
