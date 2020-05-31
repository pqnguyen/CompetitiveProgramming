class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms: return True
        notVisited = set()
        queue = collections.deque()
        queue.append(0)
        for i in range(1, len(rooms)):
            notVisited.add(i)

        while queue:
            start = queue.popleft()
            for end in rooms[start]:
                if end in notVisited:
                    notVisited.remove(end)
                    queue.append(end)

        return not notVisited
