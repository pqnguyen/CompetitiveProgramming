class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        bottom, top = 2, n
        res = [1]
        isBottom = True
        while bottom <= top:
            if k > 1:
                k -= 1
                isBottom = not isBottom
            if isBottom:
                res.append(bottom)
                bottom += 1
            else:
                res.append(top)
                top -= 1
        return res
