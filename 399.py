from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # This problem is about evaluating division expressions based on given equations and their corresponding values. The approach I used is to build a graph where each variable is a node, and the edges represent the division relationships between them. I then perform a depth-first search (DFS) for each query to find the result of the division, if possible.
        # Time complexity: O(E + Q * V) where E is the number of equations, Q is the number of queries, and V is the number of variables in the graph. The DFS may visit all nodes in the worst case for each query.
        # Space complexity: O(V) where V is the number of unique variables in the graph, as we store the graph and the explored set.
        # Performance:  
        # Runtime: faster than 100%
        # Memory Usage: beats 94.57%.
        graph = {}
        for eq, value in zip(equations, values):
            if eq[0] not in graph:
                graph[eq[0]] = []
            if eq[1] not in graph:
                graph[eq[1]] = []

            graph[eq[0]].append((eq[1], value))
            graph[eq[1]].append((eq[0], 1/value))
        result = []
        for query in queries:
            if query[0] not in graph or query[1] not in graph:
                result.append(-1.0)
                continue
            if query[0] == query[1]:
                result.append(1)
                continue
            
            explored = set()
            stack = [[query[0], 1]]
            found = -1.0
            while stack:
                start,init_val = stack.pop()
                if start not in explored:
                    for loc, val in graph[start]:
                        if loc == query[1]:
                            if found == -1.0:
                                found =init_val * val
                                result.append(found)
                            break
                        stack.append([loc, init_val * val])
                    explored.add(start)
            if found == -1.0:
                result.append(found)
        return result
