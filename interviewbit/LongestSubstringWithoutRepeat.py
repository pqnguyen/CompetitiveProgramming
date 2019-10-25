class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        tb = {}
        mxstart, mxend = 0, -1
        start, end = 0, 0
        for i, ch in enumerate(A):
            if ch in tb:
                start = max(start, tb[ch] + 1)
            if i - start > mxend - mxstart:
                mxstart, mxend = start, i
            tb[ch] = i

        return mxend - mxstart + 1


res = Solution().lengthOfLongestSubstring("")
print(res)
