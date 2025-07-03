class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # This is a sliding window problem, we can use a sliding window of size k to find the maximum number of vowels in any substring of length k.
        # We can use a set to store the vowels and then iterate through the string, keeping track of the number of vowels in the current window.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(1) : We are not using any extra space
        # Performance:
        # Runtime: faster than 97.44%.
        # Memory Usage: less than 88.63%.
        vowels = {'a', 'e', 'i', 'o', 'u'}
        # Look at the first k substring:
        curr_max = 0
        for c in s[:k]:
            if c in vowels:
                curr_max += 1
        curr_num = curr_max
        for idx in range(k, len(s)):
            if s[idx] in vowels:
                curr_num += 1
            if s[idx - k] in vowels:
                curr_num -= 1
            
            if curr_num > curr_max:
                curr_max = curr_num
        return curr_max
            