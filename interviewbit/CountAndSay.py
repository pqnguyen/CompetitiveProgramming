class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        res = "1"
        while A > 1:
            res = self.generateNext(res)
            A -= 1
        return res

    def generateNext(self, s):
        num = ""
        count = i = mark = 0
        while mark < len(s):
            while i < len(s) and s[i] == s[mark]:
                i += 1
                count += 1
            num += str(count) + s[mark]
            mark = i
            count = 0
        return num


res = Solution().generateNext("21")
print(res)
