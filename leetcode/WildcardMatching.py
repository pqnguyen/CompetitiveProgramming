class Solution:
    def isMatch(self, s, p):
        iIndex = starIndex = -1
        i = j = 0
        while i < len(s):
            if j < len(p) and (p[j] == '?' or p[j] == s[i]):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                starIndex = j
                iIndex = i
                j += 1
            elif starIndex != -1:
                j = starIndex + 1
                i = iIndex + 1
                iIndex += 1
            else:
                return False
        while j < len(p) and p[j] == '*': j += 1
        return j == len(p)


res = Solution().isMatch("mississippi", "m??*ss*?i*pi")
print(res)
