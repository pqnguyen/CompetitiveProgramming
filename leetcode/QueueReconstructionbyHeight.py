from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda person: (-person[0], person[1]))
        for i in range(len(people)):
            _, nleft = people[i]
            for index in range(i, max(nleft, 0), -1):
                people[index - 1], people[index] = people[index], people[index - 1]

        return people


res = Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
print(res)
