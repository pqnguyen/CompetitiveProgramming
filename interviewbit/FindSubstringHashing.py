class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, s, L):

        # Number of a characters of a word in list L.
        size_word = len(L[0])

        # Number of words present inside list L.
        word_count = len(L)

        # Total characters present in list L.
        size_L = size_word * word_count

        # Resultant vector which stores indices.
        res = []

        # If the total number of characters in list L
        # is more than length of string S itself.
        if size_L > len(s):
            return res

            # Map stores the words present in list L
        # against it's occurrences inside list L
        hash_map = dict()

        for i in range(word_count):
            if L[i] in hash_map:
                hash_map[L[i]] += 1
            else:
                hash_map[L[i]] = 1

        for i in range(0, len(s) - size_L + 1, 1):
            temp_hash_map = hash_map.copy()
            j = i
            count = word_count

            # Traverse the substring
            while j < i + size_L:

                # Extract the word
                word = s[j:j + size_word]

                # If word not found or if frequency of
                # current word is more than required simply break.
                if (word not in hash_map or
                        temp_hash_map[word] == 0):
                    break

                # Else decrement the count of word
                # from hash_map
                else:
                    temp_hash_map[word] -= 1
                    count -= 1
                j += size_word

                # Store the starting index of that substring
            # when all the words in the list are in substring
            if count == 0:
                res.append(i)
        return res
