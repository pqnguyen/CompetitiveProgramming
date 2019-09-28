import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums
        self.current = self.origin[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.current = self.origin[:]
        return self.current

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        ls = self.current
        for i in range(len(ls)):
            randomIndex = random.randrange(i, len(ls))
            ls[i], ls[randomIndex] = ls[randomIndex], ls[i]
        return ls


# Your Solution object will be instantiated and called as such:
obj = Solution([1, 2, 3])
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2)
