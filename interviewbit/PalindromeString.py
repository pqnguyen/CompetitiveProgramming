class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        left, right = 0, len(A) - 1
        while left < right:
            if self.valid(A[left]) and self.valid(A[right]):
                if str.lower(A[left]) != str.lower(A[right]):
                    return 0
                left += 1
                right -= 1
            elif self.valid(A[left]):
                right -= 1
            else:
                left += 1

        return 1

    def valid(self, ch):
        return ch.isalpha() or ch.isnumeric()


res = Solution().isPalindrome("A man, a plan, a canal: Panama")
print(res)
