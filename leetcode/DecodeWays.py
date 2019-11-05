class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {"": 1, "0": 0}
        return self.helper(s, dp)

    def helper(self, s, dp):
        if s in dp: return dp[s]
        res = self.helper(s[1:], dp)
        if len(s) >= 2 and '10' <= s[:2] <= '26':
            res += self.helper(s[2:], dp)
        dp[s] = res
        return res


print(Solution().numDecodings(
    "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"))
