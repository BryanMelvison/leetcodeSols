from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # This is a graph problem, I used DFS to solve this problem.
        # We can represent the cities as nodes and the connections as edges.
        # We can use a list to keep track of the explored cities.
        # We can use a queue to explore the cities, starting from the first city.
        # We will keep track of the number of provinces we have found.
        # Time complexity: O(n^2), where n is the number of cities.
        # Space complexity: O(n), where n is the number of cities, since we are using a list to store the explored cities.
        # Performance:
        # Runtime: faster than 73.20%
        # Memory Usage: less than 71.68%.
        n = len(isConnected)
        explored = [False] * n
        total_province = 0
        
        from collections import deque
        
        while all(explored) != True:
            # Look for the first unexplored and we start from there:
            current = explored.index(False)
            exploring = deque([current])
            explored[current] = True
            while exploring:
                idx = exploring.popleft()
                for i, curr in enumerate(isConnected[idx]):
                    if curr == 1 and explored[i] == False:
                        exploring.append(i)
                        explored[i] = True
                    
            total_province += 1

        return total_province

