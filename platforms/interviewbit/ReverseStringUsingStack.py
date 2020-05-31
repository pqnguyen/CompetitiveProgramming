from collections import deque


class Solution:
    # @param A : string
    # @return a strings
    def reverseString(self, A):
        stack = deque()
        for ch in A: stack.append(ch)
        res = ""
        while stack: res += stack.pop()
        return res


res = Solution().reverseString("abc")
print(res)
