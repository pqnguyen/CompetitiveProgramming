# https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1393/
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image: return image
        n, m = len(image), len(image[0])
        if image[sr][sc] == newColor: return image

        def neighbors(sr, sc):
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                r = dr + sr
                c = dc + sc
                if 0 <= r < n and 0 <= c < m:
                    yield (r, c)

        stack = collections.deque()
        stack.append((sr, sc))
        oldColor = image[sr][sc]
        image[sr][sc] = newColor
        while stack:
            sr, sc = stack.pop()
            for nr, nc in neighbors(sr, sc):
                if image[nr][nc] == oldColor:
                    image[nr][nc] = newColor
                    stack.append((nr, nc))
        return image
