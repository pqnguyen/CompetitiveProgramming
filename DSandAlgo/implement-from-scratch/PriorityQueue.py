# Sort builtin function
import heapq

tasks = [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5), (6, 4), (6, 3)]

pq = []
for task in tasks:
    heapq.heappush(pq, (-task[0], -task[1]))

while pq:
    task = heapq.heappop(pq)
    print("({},{})".format(-task[0], -task[1]), end=" ")
