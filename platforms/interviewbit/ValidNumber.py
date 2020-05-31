class Solution:
    # @param A : string
    # @return an integer
    def isNumber(self, A):
        start, end = 0, len(A) - 1
        while end >= start and A[end] == ' ': end -= 1
        while start <= end and A[start] == ' ': start += 1
        if start > end: return 0
        eidx = A.find("e", start, end)
        if eidx != -1:
            if self.isNumberHelper(A, start, eidx - 1) and self.isNumberHelper(A, eidx + 1, end, False): return 1
            return 0
        return self.isNumberHelper(A, start, end)

    def isNumberHelper(self, A, start, end, allowDot=True):
        if start <= end and A[start] == '+' or A[start] == '-': start += 1
        if A[end] == '.': return 0
        if start > end: return 0
        dot = 0
        for i in range(start, end + 1):
            if A[i] == '.' and allowDot:
                if not dot:
                    dot = 1
                else:
                    return 0
            elif not A[i].isnumeric():
                return 0
        return 1


print(Solution().isNumber("1e1"))
