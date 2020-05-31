class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        res = []
        carry = 1
        left = 0
        while left < len(A) and A[left] == 0: left += 1
        for i in range(len(A) - 1, left - 1, -1):
            total = A[i] + carry
            res.append(total % 10)
            carry = total // 10

        if carry: res.append(carry)
        return list(reversed(res))


res = Solution().plusOne([0])
print(res)
