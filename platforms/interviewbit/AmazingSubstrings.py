class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(A)
        res = 0
        for i in range(n):
            if A[i] in vowels: res += (n - i)
        return res


res = Solution().solve("ABEC")
print(res)
