from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # For this I just use recursion, I also create a set to help keep track of which elements have gone in the current list.
        # I also use a list to store the current set, and then append it to the final list when it is complete.
        # Time complexity, O(n * n!) : n! permutations, and n elements in the current set
        # Space complexity, O(n) : n elements in the current set
        # Performance:
        # Runtime: faster than 100%.
        # Memory Usage: less than 81.04%.
        list_return = []
        n = len(nums)
        def combine(current_set, set_list):
            if len(current_set) == n:
                # Using slice to instead add a copy, and not pass in reference
                list_return.append(current_set[:])
                return
            for num in nums:
                if num not in set_list:
                    current_set.append(num)
                    set_list.add(num)
                    combine(current_set, set_list)
                    current_set.pop()
                    set_list.remove(num)
        current_track = []
        explored = set()
        combine(current_track, explored)
        return list_return