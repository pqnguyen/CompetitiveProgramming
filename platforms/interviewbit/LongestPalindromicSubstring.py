class Solution:
    # @param s : string
    # @return a strings
    def longestPalindrome(self, s):
        n = len(s)
        mxlen, mxstart = 1, 0
        for i in range(n - 1):
            start = end = i
            while 0 < start and end < n - 1 and s[start - 1] == s[end + 1]:
                start -= 1
                end += 1

            if (end - start + 1 > mxlen) or (end - start + 1 == mxlen and start < mxstart):
                mxstart = start
                mxlen = end - start + 1

            if s[i] != s[i + 1]: continue
            start, end = i, i + 1
            while 0 < start and end < n - 1 and s[start - 1] == s[end + 1]:
                start -= 1
                end += 1

            if (end - start + 1 > mxlen) or (end - start + 1 == mxlen and start < mxstart):
                mxstart = start
                mxlen = end - start + 1
        return s[mxstart: mxstart + mxlen]


res = Solution().longestPalindrome("abaa")
print(res)
