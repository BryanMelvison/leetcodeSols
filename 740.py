from typing import List
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # This is a simple problem, we can just iterate through the list and keep track of the frequency of each number and then use dynamic programming to find the maximum points we can earn by deleting the numbers.
        # Time complexity: O(n + k), where n is the length of the nums list, we
        # visit each element once, and k is the maximum number in the nums list, we visit each element in the result list once.
        # Space complexity: O(n + k), we are using a dictionary to store the frequency of each number and a list to store the maximum points we can earn by deleting the numbers.
        # Performance
        # Runtime: faster than 42.95%.
        # Memory Usage: less than 31.26%.
        freq_list = {}
        max_num = max(nums)
        result = [0] * max_num

        for num in nums:
            freq_list[num] = freq_list.get(num, 0) + num
        
        for item, val in freq_list.items():
            result[item - 1] = val
        
        # now the rest is just like max robber:
        for idx in range(2, len(result)):
            if idx == 2:
                result[idx] += result[idx - 2]
            else:
                result[idx] += max(result[idx-2], result[idx - 3])


        return max(result)