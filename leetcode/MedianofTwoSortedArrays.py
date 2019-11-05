from typing import List

MAX_INT = 2 ** 31 - 1
MIN_INT = -2 ** 31


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        l1 = len(nums1)
        l2 = len(nums2)

        left, right = 0, l1
        while left <= right:
            i = (left + right) // 2
            j = (l1 + l2 + 1) // 2 - i
            print(i, j)
            maxLeftX = MIN_INT if i == 0 else nums1[i - 1]
            minRightX = MAX_INT if i == l1 else nums1[i]

            maxLeftY = MIN_INT if j == 0 else nums2[j - 1]
            minRightY = MAX_INT if j == l2 else nums2[j]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (l1 + l2) % 2 == 0:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
                return max(maxLeftX, maxLeftY)

            elif maxLeftX > minRightY:
                right = i - 1
            else:
                left = i + 1

        return 0


num1 = [1, 3]
num2 = [2]
res = Solution().findMedianSortedArrays(num1, num2)
print(res)
