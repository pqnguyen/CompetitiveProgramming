# https://leetcode.com/problems/two-city-scheduling/
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[1] - cost[0], reverse=True)
        N = len(costs)
        cost = 0
        for i in range(N // 2): cost += costs[i][0]
        for i in range(N // 2, N): cost += costs[i][1]
        return cost