# Cracking the coding interview - 3.3

# Stack of Plates: Imagine a (literal) stack of plates.
# If the stack gets too high, it might topple. Therefore, in real life,
# we would likely start a new stack when the previous stack exceeds some threshold.
# Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed
# of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks. push () and SetOfStacks. pop () should behave identically to a single stack
# (that is, pop ( ) should return the same values as it would if there were just a single stack).
# FOLLOW UP
# ImplementafunctionpopAt(int index)whichperformsapopoperationonaspecificsub-stack.
from collections import deque


class SetOfStacks:
    def __init__(self, size=10):
        self._size = size
        self.stacks = []

    def push(self, item):
        if not self.stacks or len(self.stacks[-1]) == self._size:
            self.stacks.append(deque())
        self.stacks[-1].append(item)

    def pop(self):
        if not self.stacks or len(self.stacks[-1]) == 0:
            raise Exception("stack is empty")
        tmp = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return tmp

    def popAt(self, index):
        if not self.stacks:
            return Exception("stack is empty")
        if index < 0 or index >= len(self.stacks):
            return Exception("index is out of bound")
        tmp = self.stacks[index].pop()
        for i in range(index, len(self.stacks) - 1):
            self.stacks[i].append(self.stacks[i + 1].popleft())

        if not self.stacks[-1]:
            self.stacks.pop()
        return tmp


stack = SetOfStacks(3)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
print(stack.stacks)
stack.pop()
print(stack.stacks)
stack.popAt(0)
print(stack.stacks)
