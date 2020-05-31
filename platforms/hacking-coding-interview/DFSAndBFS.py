# Cracking the coding interview - 4.1


from collections import defaultdict, deque


class Solution:
    def create_graph(self, edges, nodes):
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
        return graph

    def dfs(self, graph, visited, start, end, trace):
        visited[start] = True
        if start == end:
            return True

        for neighbor in graph[start]:
            if not visited[neighbor]:
                trace[neighbor] = start
                if self.dfs(graph, visited, neighbor, end, trace):
                    return True

        return False

    def bfs(self, graph, visited, start, end, trace):
        queue = deque()
        queue.append(start)

        while queue:
            current = queue.popleft()
            visited[current] = True
            if current == end: break
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    trace[neighbor] = current
                    queue.append(neighbor)

    def find_route(self, edges, nodes, start, end):
        graph = self.create_graph(edges, nodes)
        visited = [False] * nodes
        trace = [i for i in range(nodes)]
        self.bfs(graph, visited, start, end, trace)
        route = self.print_route(trace, visited, start, end)
        print(route)

    def print_route(self, trace, visited, start, end):
        if not visited[end]: return "no route"
        ls = []
        while end != start:
            ls.append(end)
            end = trace[end]
        ls.append(start)
        return '->'.join([str(node) for node in reversed(ls)])


edges = [
    [0, 1],
    [0, 2],
    [1, 2],
    [2, 0],
    [2, 3],
    [3, 3],
]
Solution().find_route(edges, 4, 2, 1)
