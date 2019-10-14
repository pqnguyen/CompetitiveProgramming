from collections import deque


class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        stack = deque()
        paths = A.split("/")
        for path in paths:
            if path == '.':
                continue
            elif path == '..':
                if stack: stack.pop()
            elif path:
                stack.append(path)
        res = "/" + "/".join(stack)
        return res


res = Solution().simplifyPath("/home/")
print(res)
