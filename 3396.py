class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

    # slow solution, after reading the solution I will try a more optimized solution
        # I think for our inputs, we can just track counter first
        count = {}
        for num in nums:
            if num not in count: 
                count[num] = 1
            else:
                count[num] += 1
        
        print(count)
        print(count.values())
        min_element = 0
        len_elements = len(nums)
        # Current Index = 0
        current_idx = 0
        # Check if element is distinct:
        while True:
            flag = False 
            for val in count.values():
                if val > 1:
                    # Check if we can delete
                    flag = True
            
            if flag:
                # Since true, we iterate:
                for num in nums[current_idx : current_idx + 3]:
                    count[num] -= 1
                    if count[num] == 0:
                        del count[num]
                current_idx += 3
                min_element += 1
            if not flag:
                break

        return min_element