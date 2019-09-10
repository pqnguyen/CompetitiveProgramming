# Cracking the coding interview - 4.7
# Build Order: You are given a list of projects and a list of dependencies
# (which is a list of pairs of projects, where the second project is dependent
# on the first project). All of a project's dependencies must be built before
# the project is. Find a build order that will allow the projects to be built.
# If there is no valid build order, return an error.
# SOLUTION
# EXAMPLE Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c
from collections import defaultdict


class Solution:
    def init_graph(self, projects, dependencies):
        self.incoming = {project: 0 for project in projects}
        self.graph = defaultdict(list)
        for dependency in dependencies:
            begin, end = dependency[0], dependency[1]
            self.graph[begin].append(end)
            self.incoming[end] += 1

    def get_non_incoming_nodes(self, projects):
        return [project for project in projects if self.incoming[project] == 0]

    def build_order(self, projects, dependencies):
        self.init_graph(projects, dependencies)
        non_incoming = self.get_non_incoming_nodes(projects)
        order = non_incoming[:]
        current = 0
        while current < len(order):
            neighbors = self.graph[order[current]]
            for neighbor in neighbors:
                self.incoming[neighbor] -= 1
            non_incoming = self.get_non_incoming_nodes(neighbors)
            order.extend(non_incoming)
            current += 1

        return order if len(order) == len(projects) else None


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
order = Solution().build_order(projects, dependencies)
print(order)
