# https://leetcode.com/problems/squares-of-a-sorted-array/
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        iNegative = 0
        for i in range(1, len(A)):
            if A[i] >= 0:
                iNegative = i - 1
                break
        self.reverse(A, 0, iNegative)
        for i in range(0, len(A)): A[i] *= A[i]
        res = self.merge(A, 0, iNegative, iNegative + 1, len(A) - 1)
        return res

    def reverse(self, A, begin, end):
        while begin < end:
            A[begin], A[end] = A[end], A[begin]
            begin += 1
            end -= 1

    def merge(self, A, aBegin, aEnd, bBegin, bEnd):
        res = []
        while aBegin <= aEnd and bBegin <= bEnd:
            if A[aBegin] < A[bBegin]:
                res.append(A[aBegin])
                aBegin += 1
            else:
                res.append(A[bBegin])
                bBegin += 1

        while aBegin <= aEnd:
            res.append(A[aBegin])
            aBegin += 1

        while bBegin <= bEnd:
            res.append(A[bBegin])
            bBegin += 1
        return res

