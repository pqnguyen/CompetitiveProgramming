# Cracking the coding interview - 1.6
# String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed"string would not become smaller than
# the original string, your method should return the original string. You can assume the string has only uppercase
# and lowercase letters (a - z).


class Solution:
    def compress(self, s):
        res = ''
        count = 0
        for i in range(len(s)):
            count += 1
            if i + 1 >= len(s) or s[i + 1] != s[i]:
                res += s[i] + str(count)
                count = 0
        return res


res = Solution().compress('aabcccccaaa')
print(res)
