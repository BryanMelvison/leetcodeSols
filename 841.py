from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # Remember, this is graph DFS, so for graph, remmeber to include a set to store explored
        # nodes, and a queue to explore the nodes.
        # We can use a queue to explore the rooms, starting from room 0.
        # We will keep track of the rooms we have explored in a set.
        # We will use a deque to explore the rooms, since we can append and pop from both ends efficiently.
        # Time complexity: O(n), where n is the number of rooms.
        # Space complexity: O(n), where n is the number of rooms, since we are using a set to store the explored rooms.
        # Performance:
        # Runtime: faster than 100%
        # Memory Usage: less than 74.43%.
        explored = set()

        from collections import deque
        to_explore = deque([0])

        while to_explore:
            current = to_explore.popleft()
            if current not in explored:
                explored.add(current)
                for room in rooms[current]:
                    to_explore.append(room)
            
        return len(explored) == len(rooms)