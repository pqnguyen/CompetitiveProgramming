class Solution:
    # @param A : string
    # @return a list of strings
    def restoreIpAddresses(self, A):
        res = []
        self.helper(A, 0, [], res)
        res.sort()
        return res

    def helper(self, A, start, ls, res):
        if start == len(A) and len(ls) == 4:
            res.append(".".join(ls))
            return
        num = ""
        while start < len(A):
            num += A[start]
            if int(num) > 255 or len(num) > 3 or (num != '0' and num.startswith("0")): return
            ls.append(num)
            self.helper(A, start + 1, ls, res)
            ls.pop()
            start += 1


res = Solution().restoreIpAddresses("0100100")
print(res)
