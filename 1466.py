from typing import List
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # So first idea is basically create a graph, undirected, and then with the flags, 
        # where if 1 is need to reverse, so since this is a DFS, basically we keep track the top 
        # of the tree, then see if it hasn't explored it, that means we need to reverse it, and then we add the node to the stack, and then we keep track of the explored nodes, so that we don't explore it again.
        # Time complexity: O(n) where n is the number of nodes in the graph.
        # Space complexity: O(n) since we are storing the graph in a list of lists
        # Performance:
        # Runtime: faster than 86.63%
        # Memory Usage: beats 93.05%.
        reorder = 0
        explored = set()
        # create graph (directed):
        graph = [[] for _ in range(n)]
        for connection in connections:
            graph[connection[0]].append((connection[1], 1))
            graph[connection[1]].append((connection[0], 0))

        stack = [0]
        while stack:
            idx = stack.pop()
            if idx not in explored:
                for node in graph[idx]:
                    index, flag = node
                    if index not in explored:
                        reorder += flag
                        stack.append(index)
                explored.add(idx)
        return reorder
                
