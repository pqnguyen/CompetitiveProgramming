class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        unique = set()
        unique.add("")
        self.res = 0
        self.numTilePossibilitiesUtil(tiles, [], set(), unique)
        return self.res

    def numTilePossibilitiesUtil(self, tiles, current, indices, unique):
        if len(current) > len(tiles):
            return
        key = "".join(current)
        if key not in unique:
            unique.add("".join(key))
            self.res += 1

        for i, tile in enumerate(tiles):
            if i not in indices:
                current.append(tile)
                indices.add(i)
                self.numTilePossibilitiesUtil(tiles, current, indices, unique)
                current.pop()
                indices.remove(i)


res = Solution().numTilePossibilities("ABCDEFG")
print(res)
