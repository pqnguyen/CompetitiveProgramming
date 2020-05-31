# Cracking the coding interview - 8.7
# Permutations without Dups: Write a method to compute all permutations of a string of unique chara c t ers .


class Solution:
    def permutation(self, a):
        results = []
        self.permutation_util(a, 0, results)
        print(results)
        return results

    def permutation_util(self, a, start, results):
        if start == len(a):
            results.append(a[:])
            return

        for i in range(start, len(a)):
            a[start], a[i] = a[i], a[start]
            self.permutation_util(a, start + 1, results)
            a[start], a[i] = a[i], a[start]


class Solution1:
    def permutation(self, a):
        results = self.permutation_util(a)
        print(results)
        return results

    def permutation_util(self, a):
        if not a:
            return [a]

        results = []
        ch = a[0]
        na = a[1:]
        permutations = self.permutation_util(na)
        for permutation in permutations:
            res = self.insertch(permutation, ch)
            results.extend(res)

        return results

    def insertch(self, a, ch):
        if not a: return [[ch]]
        results = []
        for i in range(len(a) + 1):
            na = a[:i] + [ch] + a[i:]
            results.append(na[:])
        return results


a = [1, 2, 3]
Solution().permutation(a)
Solution1().permutation(a)
