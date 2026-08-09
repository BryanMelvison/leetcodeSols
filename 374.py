# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    # Time complexity: O(log n) since we are using binary search to find the picked number.
    # Space complexity: O(1) since we are using constant space to store the left
    # and right pointers.
    # Performance:
    # Runtime: faster than 66.94%
    # Memory Usage: beats 94.10%.
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2
            result = guess(mid)
            if result == 0:
                return mid
            elif result > 0:
                left = mid + 1
            else: 
                right = mid - 1

        return left

