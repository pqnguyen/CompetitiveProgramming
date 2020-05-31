from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        phone = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = self.helper(digits, 0, phone)
        return res

    def helper(self, digits, index, phone):
        if index >= len(digits): return ['']
        digit = digits[index]
        res = []
        rest = self.helper(digits, index + 1, phone)
        if not phone[digit]: return rest
        for ch in phone[digit]:
            for ele in rest:
                res.append(ch + ele)
        return res


res = Solution().letterCombinations("")
print(res)
