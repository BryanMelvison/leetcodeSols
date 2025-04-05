from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Store in dict, arrange the strings according to how the characters of each strings can be sorted ascendingly.
        # let n: number of strings and k: average length of string
        # Time complexity, O(n* k *logk) : Sorting: klog(k), iterate over n strings
        # Space complexity, O(n * k) : length of dict(n) * average length of string (k)

        # Performance:
        # Runtime: faster than 98.01%.
        # Memory Usage: less than 95.69%.

        anagram = {}
        for string in strs:
            sort = "".join(sorted(string))
            if sort in anagram:
                anagram[sort].append(string)
            else:
                anagram[sort] = [string]
        
        return list(anagram.values())
        