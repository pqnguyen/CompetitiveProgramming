class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        good_words = set(A.split("_"))
        reviews = []
        for i, review in enumerate(B):
            reviews.append((self.getPoint(review, good_words), i))
        reviews.sort(key=lambda review: (-review[0], review[1]))
        return [review[1] for review in reviews]

    def getPoint(self, review, good_words):
        review_words = review.split("_")
        point = 0
        for word in review_words:
            if word in good_words: point += 1
        return point


S = "cool_ice_wifi"
R = ["water_is_cool", "cold_ice_drink", "cool_wifi_speed"]
res = Solution().solve(S, R)
print(res)
