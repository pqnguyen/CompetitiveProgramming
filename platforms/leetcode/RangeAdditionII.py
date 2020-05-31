class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row = min([op[0] for op in ops], default=m)
        min_col = min([op[1] for op in ops], default=n)
        return min_row * min_col
