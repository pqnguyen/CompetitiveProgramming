class Solution:
    def calculate(self, s: str) -> int:
        a = self.string2list(s)
        ls = []
        i = 0
        while i < len(a):
            if a[i] in ('*', '/'):
                prev = ls.pop()
                next = a[i + 1]
                if a[i] == '*':
                    val = prev * next
                else:
                    val = prev // next
                ls.append(val)
                i += 2
            else:
                ls.append(a[i])
                i += 1
        res = ls[0]
        for i in range(1, len(ls), 2):
            if ls[i] == '+':
                res += ls[i + 1]
            else:
                res -= ls[i + 1]
        return res

    def string2list(self, s):
        ls = []
        s = s.replace(" ", "")
        i = 0
        num = 0
        while i < len(s):
            ch = s[i]
            if ch not in ('+', '-', '*', '/'):
                num = num * 10 + int(ch)

            if ch in ('+', '-', '*', '/'):
                ls.append(num)
                ls.append(ch)
                num = 0

            if i == len(s) - 1: ls.append(num)
            i += 1
        return ls


res = Solution().calculate("  3+2*2/2")
print(res)
