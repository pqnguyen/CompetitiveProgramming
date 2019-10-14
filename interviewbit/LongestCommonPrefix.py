class Solution:
    # @param A : list of strings
    # @return a strings
    def longestCommonPrefix(self, A):
        if not A: return ""
        prefix = ""
        i = 0
        while i < len(A[0]):
            ch = A[0][i]
            for s in A:
                if i >= len(s) or s[i] != ch:
                    return prefix
            prefix += ch
            i += 1
        return prefix


res = Solution().longestCommonPrefix(["ABCD"])
print(res)
