# https://leetcode.com/problems/valid-mountain-array/
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        index = 1
        while index < len(A) and A[index] > A[index - 1]: index += 1
        if index == 1 or index == len(A): return False
        while index < len(A) and A[index] < A[index - 1]: index += 1
        return index == len(A)
