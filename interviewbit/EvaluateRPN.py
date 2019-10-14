from collections import deque


class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = deque()
        for num in A:
            if num in {'+', '-', "*", "/"}:
                second, first = int(stack.pop()), int(stack.pop())
                if num == "+":
                    res = first + second
                elif num == "-":
                    res = first - second
                elif num == "*":
                    res = first * second
                else:
                    res = first // second
                stack.append(res)
            else:
                stack.append(int(num))
        return int(stack.pop())


exp = ["4", "13", "5", "/", "+"]
res = Solution().evalRPN(exp)
print(res)
