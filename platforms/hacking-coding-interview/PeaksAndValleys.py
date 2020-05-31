# Cracking the coding interview - 10.11
# Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal
# to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent
# integers. For example, in the array {S, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {S, 2} are valleys.
# Given an array of integers, sort the array into an alternating sequence of peaks and valleys.
# EXAMPLE
# Input: {S, 3, 1,2, 3}
# Output: {S, 1,3,2, 3}


class Solution:
    def sort_peaks_and_valleys(self, a):
        for i in range(1, len(a)):
            if (i % 2 == 0 and a[i - 1] > a[i]) or (i % 2 == 1 and a[i - 1] < a[i]):
                a[i - 1], a[i] = a[i], a[i - 1]
        return a


res = Solution().sort_peaks_and_valleys([5, 4, 3, 2, 1, 6])
print(res)
