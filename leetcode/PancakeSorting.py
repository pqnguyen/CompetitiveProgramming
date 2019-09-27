from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        n = len(A)
        indices = {}
        for index, val in enumerate(A): indices[val] = index
        res = []
        for i in range(n - 1, -1, -1):
            correctNumber = n - i
            if A[i] == correctNumber: continue
            if indices[correctNumber] + 1 > 1:
                res.append(indices[correctNumber] + 1)
                self.reverse(A, 0, indices[correctNumber], indices)
            res.append(i + 1)
            self.reverse(A, 0, i, indices)
        res.append(n)
        return res

    def reverse(self, A, left, right, indices):
        while left < right:
            indices[A[left]] = right
            indices[A[right]] = left
            A[left], A[right] = A[right], A[left]
            left += 1
            right -= 1


res = Solution().pancakeSort([1, 2, 3])
print(res)
