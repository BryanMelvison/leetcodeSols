class Solution:
    def numTilings(self, n: int) -> int: 
        # This problem is about counting the number of ways to tile a 2 x n board using 2 x 1 dominoes and "L" shaped trominoes. The approach I used is dynamic programming, where I maintain a dictionary to store the number of ways to tile boards of different lengths. The recurrence relation is derived from the fact that for each length n, we can either place a vertical domino (which leaves us with a board of length n-1), place two horizontal dominoes (which leaves us with a board of length n-2), or place an "L" shaped tromino (which leaves us with a board of length n-3). The final answer is computed modulo 10^9 + 7 to prevent overflow.
        # Time complexity: O(n) where n is the length of the board.
        # Space complexity: O(n) since we are storing the number of ways to tile boards
        # of different lengths in a dictionary.
        # Performance:
        # Runtime: faster than 53.38%
        # Memory Usage: beats 49.94%.
        MOD = 10**9 + 7       
        dictionary = {0: 1, 1: 1, 2: 2}
        for idx in range(3, n + 1):
            dictionary[idx] = (2 *dictionary[idx-1] + dictionary[idx-3]) % MOD
        
        return dictionary[n]