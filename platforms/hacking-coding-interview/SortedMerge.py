# Cracking the coding interview - 10.1
# Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer
# at the end to hold B. Write a method to merge Binto A in sorted order.


class Solution:
    def merge(self, a, b, lastA, lastB):
        end_index = lastA + lastB - 1
        indexA = lastA - 1
        indexB = lastB - 1
        while indexA > -1 and indexB > -1:
            if a[indexA] > b[indexB]:
                a[end_index] = a[indexA]
                indexA -= 1
            else:
                a[end_index] = b[indexB]
                indexB -= 1
            end_index -= 1

        while indexA > -1:
            a[end_index] = a[indexA]
            indexA -= 1
            end_index -= 1

        while indexB > -1:
            a[end_index] = b[indexB]
            indexB -= 1
            end_index -= 1


a = [2, 3, 4, 0, 0, 0, 0, 0]
b = [1, 2, 5, 6, 7]
Solution().merge(a, b, 3, 5)
print(a)
