class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        if not A: return -1
        count = 1
        val = A[0]
        for i in range(1, len(A)):
            if count == 0: val = A[i]
            if A[i] == val:
                count += 1
            else:
                count -= 1
        return val


res = Solution().majorityElement([2, 1, 2, 1, 1])
print(res)
