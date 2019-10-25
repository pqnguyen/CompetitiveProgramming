class Solution:
    # @param A : string
    # @return a list of strings
    def letterCombinations(self, A):
        phone = {
            '0': '0',
            '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        self.letterCombinationsHelper(phone, A, 0, "", res)
        res.sort()
        return res

    def letterCombinationsHelper(self, phone, A, index, current, res):
        if index == len(A):
            res.append(current)
            return

        if A[index] not in phone: return
        for ch in phone[A[index]]:
            self.letterCombinationsHelper(phone, A, index + 1, current + ch, res)


res = Solution().letterCombinations("23")
print(res)
