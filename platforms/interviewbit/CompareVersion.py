class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        a = list(map(int, A.split('.')))
        b = list(map(int, B.split('.')))
        while a[-1] == 0: a.pop()
        while b[-1] == 0: b.pop()

        for i in range(min(len(a), len(b))):
            if a[i] < b[i]:
                return -1
            elif a[i] > b[i]:
                return 1
        if len(a) > len(b):
            return 1
        elif len(a) < len(b):
            return -1
        return 0


res = Solution().compareVersion("1.1", "1.1.1")
print(res)
