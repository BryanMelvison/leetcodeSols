
from ast import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # FOr this, draw the recursion depth first, and then understand where can we prune, we can use a map to store the minimum cost for each day, and then we can use that to prune the recursion tree.
        # Time complexity: O(n), where n is the length of the days list, we
        # visit each element once.
        # Space complexity: O(n), we are using a map to store the minimum cost for
        # each day.
        # Performance:
        # Runtime: faster than 37.79%.
        # Memory Usage: less than 19.44%.
        cost = {}
        def dfs(i):
            if i >= len(days):
                return 0
            if i in cost:
                return cost[i]
            cost[i] = float("inf")
            j = i
            for c, d in zip(costs, [1, 7, 30]):
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                cost[i] = min(cost[i], c + dfs(j))
            return cost[i]

        return dfs(0)