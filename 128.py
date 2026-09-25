class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Just normal solution, we can use a set to store the numbers and then for each number, we can check if it is the start of a sequence by checking if the number - 1 is not in the set. If it is the start of a sequence, we can then iterate through the sequence and count the length of the sequence. Finally, we can return the maximum length of the sequences we have found.
        # Time complexity: O(n), where n is the length of the nums list, we
        # visit each element once.
        # Space complexity: O(n), we are using a set to store the numbers we have
        # seen so far.
        # Performance:
        # Runtime: faster than 96.42%.
        # Memory Usage: less than 20.62%.
        num_set = set(nums)
        total = 0
        for num in num_set:
            if num + 1 in num_set:
                continue
            local_total = 1
            current = num - 1
            while current in num_set:
                local_total += 1
                current -= 1
            total = max(total, local_total)
        return total                