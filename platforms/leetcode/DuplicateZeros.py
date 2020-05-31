# https://leetcode.com/problems/duplicate-zeros/
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        index = mark = needed = 0
        for i in range(n):
            if arr[i]:
                needed += 1
            else:
                needed += 2
            if needed >= n:
                if arr[i] == 0 and needed == n:
                    arr[-2] = arr[-1] = 0
                    mark = i - 1
                    index = n - 3
                else:
                    arr[-1] = arr[i]
                    mark = i - 1
                    index = n - 2
                break
        while index > 0:
            if arr[mark]:
                arr[index] = arr[mark]
                index -= 1
            else:
                arr[index] = arr[index - 1] = 0
                index -= 2
            mark -= 1
