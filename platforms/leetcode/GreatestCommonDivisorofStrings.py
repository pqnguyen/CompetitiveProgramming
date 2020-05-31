# https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        indexFirstCh = []
        for i in range(1, len(str1)):
            if str1[i] == str1[0]:
                indexFirstCh.append(i)
        indexFirstCh.append(len(str1))
        n, m = len(str1), len(str2)
        for index in reversed(indexFirstCh):
            divisor = str1[:index]
            t1 = n % len(divisor)
            if not (t1 == 0 and divisor * (n // len(divisor)) == str1):
                continue
            t1 = m % len(divisor)
            if not (t1 == 0 and divisor * (m // len(divisor)) == str2):
                continue
            return divisor
        return ""

    def gcdOfStringsBetter(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return str1 if str1 else str2
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        elif str1[: len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return ''
