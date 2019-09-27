# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq


class Solution:
    def generalizedAbbreviation(self, word):
        res = []
        self.generalizedAbbreviationUtil(list(word), 0, "", res)
        return res

    def generalizedAbbreviationUtil(self, letters, index, abb, res):
        if index >= len(letters):
            res.append(abb)
            return

        for length in range(len(letters) - index + 1):
            nextIndex = index + length + 1
            nabb = abb
            if length != 0:
                nabb += str(length)
            if nextIndex <= len(letters):
                nabb += letters[nextIndex - 1]
            self.generalizedAbbreviationUtil(letters, nextIndex, nabb, res)


res = Solution().generalizedAbbreviation("word")
print(res)
