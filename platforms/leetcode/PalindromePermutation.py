from collections import Counter


class Solution:
    def canPermutePalindrome(self, s):
        counter = Counter(s)
        odd = False
        for ch, count in counter.items():
            if count % 2 == 1:
                if not odd:
                    odd = True
                else:
                    return False
        return True


res = Solution().canPermutePalindrome("aaabb")
print(res)
