from typing import List
class Solution:
    # This problem is about finding all unique permutations of a list of numbers that may contain duplicates.
    # We will use backtracking to generate permutations and a set to avoid duplicates.
    # Time complexity: O(n * n!) in the worst case where n is the number of elements in nums.
    # Space complexity: O(n) for the recursion stack and the result list.
    # Performance:
    # Runtime: faster than 100%
    # Memory Usage: less than 18.68%.
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        def permute(current, temp):
            prev = None
            if current:                    
                for idx, curr in enumerate(current):
                    if prev == curr:
                        continue
                    else:
                        temp.append(curr)
                        res = current[:idx] + current[idx + 1: ] # Remove the current unit from the list (not remove like remove, just create new list)
                        prev = curr # Also very important, this helps track so there aren't duplicates call to the permutation stack
                        permute(res, temp)
                        temp.pop() # Backtrack if out of stack
    
            else:
                result.append(temp[:])     

        permute(nums, [])
        return result
