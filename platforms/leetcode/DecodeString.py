import collections


class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = collections.deque()
        for ch in s:
            if ch == ']':
                encoded = ''
                while stack[-1] != '[': encoded = stack.pop() + encoded
                stack.pop()
                k = ''
                while stack and '0' <= stack[-1] <= '9': k = stack.pop() + k
                stack.append(encoded * int(k))
            else:
                stack.append(ch)
        res = "".join(stack)
        return res


res = Solution().decodeString("2[abc]3[cd]ef")
print(res)
