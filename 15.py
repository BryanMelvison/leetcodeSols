from typing import List

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # SO for this one, I used a hash map to store the numbers, and then for each number, I will check if the target - nums[i] - nums[j] is in the hash map, if it is, then we have a triplet, and we can add it to the result.
        # Time complexity, O(n^2) : Just two for loops
        # Space complexity, O(n) : store at most n elements in the hash map
        # Performance:
        # Runtime: faster than 18.06%
        # Memory Usage: beats 81.44%.
        nums.sort()
        total = len(nums)
        result = []
        target = 0
        prev = None
        for i in range(total):
            local_target = target - nums[i]
            # With a bit of memoization too
            if prev == nums[i]:
                continue
            current_history = {}
            record = set()
            if i + 2 == total:
                break
            for j in range(i + 1, total):
                if local_target - nums[j] in current_history:
                    if (nums[i], current_history[local_target - nums[j]], nums[j]) not in record:
                        result.append([nums[i], current_history[local_target - nums[j]], nums[j]])
                        record.add((nums[i], current_history[local_target - nums[j]], nums[j]))
                else:
                    current_history[nums[j]] = nums[j]
            prev = nums[i]
        return result
