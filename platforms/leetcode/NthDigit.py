class Solution:
    def findNthDigit(self, n: int) -> int:
        length, start, count = 1, 1, 9
        while n > length * count:
            n -= length * count
            length += 1
            count *= 10
            start *= 10

        start += (n - 1) // length
        return int(str(start)[(n - 1) % length])


res = Solution().findNthDigit(15)
print(res)
