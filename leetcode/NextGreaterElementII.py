class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        length = len(nums)
        nums.extend(nums[:])
        stack, res = [], [-1] * len(nums)
        for index, num in enumerate(nums):
            while stack and num > stack[-1][1]:
                i, n = stack.pop()
                res[i] = num
            stack.append((index, num))
        return res[:length]
