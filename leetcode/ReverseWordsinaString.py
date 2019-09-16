# https://leetcode.com/explore/learn/card/array-and-string/204/conclusion/1164/
class Solution:
    def reverseWords(self, s: str) -> str:
        a = []
        needSpace = False
        for ch in s:
            if ch != ' ':
                a.append(ch)
                needSpace = True
            elif needSpace:
                needSpace = False
                a.append(' ')
        while a and a[-1] == ' ': a.pop()
        self.reverse(a, 0, len(a) - 1)
        start = 0
        for i in range(len(a)):
            if a[i] == ' ':
                self.reverse(a, start, i - 1)
                start = i + 1
        self.reverse(a, start, len(a) - 1)
        return "".join(a)

    def reverse(self, a, start, end):
        while start < end:
            a[start], a[end] = a[end], a[start]
            start += 1
            end -= 1


res = Solution().reverseWords("  make good   example")
print(res)
