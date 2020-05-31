# Cracking the coding interview - 3.5

# Sort Stack: Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements into any other
# data structure (such as an array). The stack supports the following operations:
# push, pop, peek, and isEmpty

from collections import deque as Stack


class TemporaryStackSolution:
    def sort_stack(self, stack):
        result = Stack()

        while stack:
            top = stack.pop()
            while result and result[-1] < top:
                stack.append(result.pop())
            result.append(top)

        return result


class RecursiveSolution:
    def sort_stack(self, stack):
        if not stack: return
        top = stack.pop()
        self.sort_stack(stack)
        self.insert_sort(top, stack)

    def insert_sort(self, top, stack):
        if stack and top > stack[-1]:
            ele = stack.pop()
            self.insert_sort(top, stack)
            stack.append(ele)
        else:
            stack.append(top)


stack = Stack()
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack = TemporaryStackSolution().sort_stack(stack)
# RecursiveSolution().sort_stack(stack)
print(stack)
