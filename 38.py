class Solution:
    def countAndSay(self, n: int) -> str:
        # Just keep track of the number, and count the number of times it appears, and append to the string
        # Time complexity, O(2^n) : Each iteration doubles the length of the string
        # Space complexity, O(2^n) : store at most 2^n elements in the string
        # Performance:
        # Runtime: faster than 91.36%
        # Memory Usage: beats 15.89%.

        found = {1: "1"}

        def count_up(number):
            local_count = 0
            local_value = ""
            max_value = ""
            for num in found[number]:
                if num != local_value:
                    if local_value != "":
                        max_value += str(local_count) + local_value
                    local_value = num
                    local_count = 1
                else:
                    local_count += 1

            return max_value + str(local_count) + local_value
        if n in found:
            return found[n]
        
        for current in range(2, n + 1):
            value = count_up(current - 1)
            found[current] = value
        
        return found[n]
