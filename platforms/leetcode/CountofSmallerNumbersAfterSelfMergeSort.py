from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)

        def mergesort(enum):
            half = len(enum) // 2
            if half:
                left, right = mergesort(enum[:half]), mergesort(enum[half:])
                for i in range(len(enum)):
                    if not right or left and left[0][1] > right[0][1]:
                        counts[left[0][0]] += len(right)
                        enum[i] = left.pop(0)
                    else:
                        enum[i] = right.pop(0)

            return enum

        mergesort(list(enumerate(nums)))
        return counts


res = Solution().countSmaller([5, 4, 3, 5, 1])
print(res)
