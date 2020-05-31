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
from collections import defaultdict, deque
from enum import Enum


class Status(Enum):
    Blank = 0
    Partial = 1
    Completed = 2


class Solution:
    def init_graph(self, projects, dependencies):
        self.status = {project: Status.Blank for project in projects}
        self.graph = defaultdict(list)
        for dependency in dependencies:
            begin, end = dependency[0], dependency[1]
            self.graph[begin].append(end)

    def build_order(self, projects, dependencies):
        self.init_graph(projects, dependencies)
        result = deque()
        for project in projects:
            if self.status[project] == Status.Blank:
                self.dfs(project, result)
        return result

    def dfs(self, project, result):
        if self.status[project] == Status.Partial: raise Exception('circular dependencies')
        if self.status[project] == Status.Blank:
            self.status[project] = Status.Partial
            neighbors = self.graph[project]
            for neighbor in neighbors:
                self.dfs(neighbor, result)
            self.status[project] = Status.Completed
            result.appendleft(project)


projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
order = Solution().build_order(projects, dependencies)
print(order)
