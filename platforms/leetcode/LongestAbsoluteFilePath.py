class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input += '\n'
        paths = []
        currentFile = ""
        maxLength = level = 0
        length = -1
        for ch in input:
            if ch == '\n':
                while paths and paths[-1][1] >= level:
                    top = paths.pop()
                    length = length - len(top[0]) - 1

                paths.append((currentFile, level))
                length = length + 1 + len(currentFile)
                if "." in currentFile:
                    maxLength = max(maxLength, length)

                currentFile = ""
                level = 0
            elif ch == '\t':
                level += 1
            else:
                currentFile += ch
        return maxLength


res = Solution().lengthLongestPath(
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
print(res)
