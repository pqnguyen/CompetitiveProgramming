class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A.sort()
        MOD = int(1e9) + 7
        count = 0
        for k in range(len(A) - 1, 1, -1):
            i, j = 0, k - 1
            while i < j:
                if A[i] + A[j] > A[k]:
                    count += (j - i)
                    j -= 1
                else:
                    i += 1
                count %= MOD
        return count % MOD


res = Solution().nTriang([4, 6, 13, 16, 20, 3, 1, 12])
print(res)
