class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, A, B):
        sign = -1
        if (A <= 0 and B <= 0) or (A >= 0 and B >= 0): sign = 1
        A, B = abs(A), abs(B)
        res = str(A // B)
        remainder = A % B
        index = -1
        if remainder:
            res += '.'
            tb = {remainder: len(res)}
            while remainder:
                num = remainder * 10 // B
                res += str(num)
                remainder = remainder * 10 % B
                if remainder in tb:
                    index = tb[remainder]
                    break
                tb[remainder] = len(res)
        if index != -1:
            res = res[:index] + '(' + res[index:] + ')'
        if sign < 0: res = '-' + res
        return res


res = Solution().fractionToDecimal(-1, -2)
print(res)
