class Solution:
    def complexNumberMultiply(self, x: str, y: str) -> str:
        a, b = self.seperate(x)
        ap, bp = self.seperate(y)
        left = a * ap - b * bp
        right = a * bp + ap * b
        return "{}+{}i".format(left, right)

    def seperate(self, complex):
        a, b = complex.split('+')
        return int(a), int(b.replace('i', ''))


res = Solution().complexNumberMultiply("1+1i", "1+1i")
print(res)
