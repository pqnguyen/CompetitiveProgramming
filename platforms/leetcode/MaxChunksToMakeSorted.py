class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        arr.append(len(arr))
        indices = {val: index for index, val in enumerate(arr)}
        m = res = 0
        for i in range(len(arr)):
            if i > m: res += 1
            m = max(m, indices[i])
        return res
