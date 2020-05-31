# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sumEven = sum(e for e in A if e % 2 == 0)
        res = []
        for val, index in queries:
            if A[index] % 2 == 0:
                sumEven -= A[index]
            A[index] += val
            if A[index] % 2 == 0:
                sumEven += A[index]
            res.append(sumEven)
        return res

