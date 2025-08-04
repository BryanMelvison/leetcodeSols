from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # This is a sliding window problem, we just need to keep track of the number of distinct fruits in the window.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(1) : We only need to store the number of distinct fruits in the window (At most 3 elements)
        # Performance:
        # Runtime: faster than 74.44%
        # Memory Usage: less than 77.01%.
        maxNumber = 0
        left = 0
        dupl = {}
        for right in range(len(fruits)):
            if fruits[right] in dupl:
                dupl[fruits[right]] += 1
            else:
                dupl[fruits[right]] = 1
                # Skip this if less than 2
                while len(dupl) > 2:
                    dupl[fruits[left]] -= 1

                    if dupl[fruits[left]] == 0:
                        del dupl[fruits[left]]
                    left += 1
                
            maxNumber = max(right - left + 1, maxNumber)
        return maxNumber