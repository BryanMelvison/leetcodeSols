from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # For this I need 2 queues:
        # One for Radiant and one for Dire, and I will keep track of the index of the senators, and if one senator is banned, I will add them back to the queue with an incremented index
        # Time complexity, O(n) : We need to iterate through the senate string to create the queues and then process them
        # Space complexity, O(n) : We are using two deques to store the indices of the senators
        # Performance:
        # Runtime: faster than 48.66%
        # Memory Usage: less than 19.96%.
        radiant = deque()
        dire = deque()
        n = len(senate)

        for idx, sen in enumerate(senate):
            if sen == "R":
                radiant.append(idx)
            else:
                dire.append(idx)
        
        while radiant and dire:
            curr_rad = radiant.popleft()
            curr_dir = dire.popleft()

            if curr_rad < curr_dir:
                radiant.append(curr_rad + n)
            else:
                dire.append(curr_dir + n)
        return "Radiant" if radiant else "Dire"
