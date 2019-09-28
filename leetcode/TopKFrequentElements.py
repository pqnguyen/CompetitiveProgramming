from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        a = list(counter.items())
        self.sortklargest(a, 0, len(a) - 1, k, key=lambda item: item[1])
        return [item[0] for item in a[:k]]

    def sortklargest(self, a, left, right, k, key):
        if left > right: return
        mid = self.partition(a, left, right, key)
        if mid > k:
            self.sortklargest(a, left, mid - 1, k, key)
        else:
            self.sortklargest(a, left, mid - 1, k, key)
            self.sortklargest(a, mid + 1, right, k, key)

    def partition(self, a, left, right, key):
        wall = left
        for i in range(left, right):
            if key(a[i]) > key(a[right]):
                a[wall], a[i] = a[i], a[wall]
                wall += 1
        a[wall], a[right] = a[right], a[wall]
        return wall


a = [1, 1, 1, 2, 2, 3, 3, 3, 3, 2, 2, 1, 1]
res = Solution().topKFrequent(a, 2)
print(res)
