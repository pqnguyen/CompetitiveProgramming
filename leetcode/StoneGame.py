def stoneGame(piles):
    cache = {}

    def firstscore(i, j):
        if i == j: return piles[i]
        if j == i + 1: return max(piles[i], piles[j])
        if (i, j) in cache: return cache[i, j]
        res = max(
            piles[i] + min(firstscore(i + 2, j), firstscore(i + 1, j - 1)),
            piles[j] + min(firstscore(i + 1, j - 1), firstscore(i, j - 2))
        )
        cache[i, j] = res
        return res

    Alex = firstscore(0, len(piles) - 1)
    Lee = sum(piles) - Alex
    print(Alex, Lee)
    return Alex > Lee


stoneGame([8, 15, 3, 7])
