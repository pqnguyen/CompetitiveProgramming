class Solution:
    def rangeAddition(self, length, updates):
        a = [0] * length
        for start, end, val in updates:
            a[start] += val
            if end + 1 < length:
                a[end + 1] += (-1 * val)

        for i in range(1, length): a[i] += a[i - 1]
        return a


length = 5
updates = [
    [1, 3, 2],
    [2, 4, 3],
    [0, 2, -2]
]
res = Solution().rangeAddition(length, updates)
print(res)
