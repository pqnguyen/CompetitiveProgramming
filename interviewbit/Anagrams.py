from collections import defaultdict


class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        tb = defaultdict(list)
        words = A.split(" ")
        for i, word in enumerate(words):
            key = "".join(sorted(word))
            tb[key].append(i + 1)
        res = []
        for key, ls in tb.items(): res.append(ls)
        res.sort()
        return res


res = Solution().anagrams("cat dog god tca")
print(res)
