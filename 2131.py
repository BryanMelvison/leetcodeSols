from typing import List

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        # For this I break it down into 2 types of problems (Symmetric, and Asymmetric), and for symmetric it can be a palindrome of itself, so I first count how many can be palindromic pairs, and then have a flag for center piece, same logic for asymmetric without center piece
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the dict
        # Performance:
        # Runtime: faster than 83.21%.
        # Memory Usage: less than 40.25%.


        from collections import Counter

        count = Counter(words)
        
        total = 0 
        # Individual flag:
        indiv = True
        for k,v in count.items():
            if k[0] == k[1]:
                res = v//2
                total += res *4
                if v % 2 == 1:
                    if indiv:
                        total += 2
                        indiv = False
            else:
                if count[k[1]+k[0]]:
                    if count[k[1] + k[0]] != 0 or count[k] != 0:
                        min_tot = min(count[k], count[k[1] + k[0]])
                        total +=min_tot  * 4
                        count[k] -= min_tot
                        count[k[1] + k[0]] -= min_tot
        return total



        
