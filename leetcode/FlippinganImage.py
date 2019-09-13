# https://leetcode.com/problems/flipping-an-image/
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            self.flipRow(row)
        return A

    def flipRow(self, row):
        left, right = 0, len(row) - 1
        while left < right:
            row[left], row[right] = int(not row[right]), int(not row[left])
            left += 1
            right -= 1

        if left == right: row[left] = int(not row[left])
