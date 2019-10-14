class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        i = len(A) - 1
        while i >= 0 and A[i] == ' ': i -= 1
        j = i
        while j >= 0 and A[j].isalpha(): j -= 1
        return i - j


res = Solution().lengthOfLastWord("world   ")
print(res)
