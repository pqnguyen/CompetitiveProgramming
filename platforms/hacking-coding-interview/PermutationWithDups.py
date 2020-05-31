# Cracking the coding interview - 8.8
# Permutations with Duplicates: Write a method to compute all permutations of a string
# whose characters are not necessarily unique. The list of permutations should not have duplicates.
from collections import defaultdict


class Solution:
    def permutation(self, a):
        freq = self.count_freq(a)
        results = []
        self.permutation_util(a, freq, results, [])
        print(results)
        return results

    def permutation_util(self, a, freq, results, current):
        if len(current) == len(a):
            results.append(current[:])
            return

        for key in freq.keys():
            if freq[key]:
                freq[key] -= 1
                current.append(key)
                self.permutation_util(a, freq, results, current)
                current.pop()
                freq[key] += 1

    def count_freq(self, a):
        freq = defaultdict(int)
        for e in a: freq[e] += 1
        return freq


a = [1, 1, 2, 3]
Solution().permutation(a)
