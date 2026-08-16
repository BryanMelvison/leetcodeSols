from typing import List
class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Create Adjacency List, perform DFS to find all reachable nodes from k, then check if any of the unreachable nodes have an edge to a reachable node. If so, return all nodes, else return the unreachable nodes.
        # Time Complexity: O(n + m), where n is the number of nodes and m is the number of edges
        # Space Complexity: O(n + m), where n is the number of nodes and m is the number of edges
        # Performance:
        # Runtime: faster than 22.63%.
        # Memory Usage: less than 31.57%.
        adj_list = {idx: [] for idx in range(n)}
        for invok in invocations:
            adj_list[invok[0]].append(invok[1])
        
        stack = [k]
        explored = set()

        while stack:
            current = stack.pop(-1)
            if current not in explored:
                for num in adj_list[current]:
                    if num not in explored:
                        stack.append(num)

                explored.add(current)
        full_list = [_ for _ in range(n)]
        all_idx = set(full_list) - explored
        if len(all_idx) == 0:
            return []

        for idx in all_idx:
            for item in adj_list[idx]:
                if item in explored:
                    return full_list
        return list(all_idx)


