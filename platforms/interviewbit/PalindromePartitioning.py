class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, s):
        res = []
        self.partitionHelper(s, 0, [], res)
        res.sort()
        return res

    def partitionHelper(self, s, index, current, res):
        if index == len(s):
            res.append(current[:])
            return

        for i in range(index, len(s)):
            if self.isPalindrome(s, index, i):
                current.append(s[index:i + 1])
                self.partitionHelper(s, i + 1, current, res)
                current.pop()

    def isPalindrome(self, s, start, end):
        if not s: return False
        while start < end:
            if s[start] != s[end]: return False
            start += 1
            end -= 1
        return True


res = Solution().partition("aaa")
print(res)
