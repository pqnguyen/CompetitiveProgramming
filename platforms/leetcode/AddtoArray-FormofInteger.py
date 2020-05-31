# https://leetcode.com/problems/add-to-array-form-of-integer/
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        carry = 0
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = A[i] // 10, A[i] % 10
            if i: A[i - 1] += carry
        if carry:
            A = list(map(int, list(str(carry)))) + A
        return A
