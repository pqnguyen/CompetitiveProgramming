import heapq


class Solution:
    # @param arrive : list of integers
    # @param depart : list of integers
    # @param K : integer
    # @return a boolean
    def hotel(self, arrive, depart, K):
        room = 0
        heap = []
        visitors = [(arrive[i], depart[i]) for i in range(len(arrive))]
        visitors.sort(key=lambda vistor: (vistor[0], vistor[1]))
        for i in range(len(visitors)):
            if visitors[i][0] == visitors[i][1]: continue
            if not heap or heap[0] > visitors[i][0]:
                heapq.heappush(heap, visitors[i][1])
                room += 1
            else:
                _ = heapq.heappop(heap)
                heapq.heappush(heap, visitors[i][1])

        return room <= K


res = Solution().hotel([40, 18], [40, 43], 1)
print(res)
