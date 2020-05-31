# Cracking the coding interview - 1.7
# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
# write a method to rotate the image by 90 degrees. Can you do this in place?


class Solution:
    def rotate_matrix(self, a):
        if not len(a) or len(a) != len(a[0]): return False
        n = len(a)
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            for i in range(first, last):
                offset = i - first
                top = a[first][i]  # save top
                a[first][i] = a[last - offset][first]  # left -> top
                a[last - offset][first] = a[last][last - offset]  # bottom -> left
                a[last][last - offset] = a[i][last]  # right -> bottom
                a[i][last] = top


a = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
Solution().rotate_matrix(a)
for sa in a:
    print(sa)
