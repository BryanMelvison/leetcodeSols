class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # So for this problem, I used a greedy approach to get the smallest lexicographical order of the string, I kept track of the count of each character in the string, and a set to keep track of the characters that have been added to the result. For each character, if it has not been added to the result, I will check if it is smaller than the last character in the result and if the last character can be found later in the string, if so, I will remove the last character from the result and add the current character to the result.
        # Time complexity, O(n) : Just one for loop
        # Space complexity, O(n) : store at most n elements in the result and thde count_map
        # Performance:
        # Runtime: faster than 70.62%
        # Memory Usage: beats 45.48%.
        result = []
        count_map = {}
        seen = set()
        # create map first
        for char in s:
            count_map[char] = count_map.get(char, 0) + 1

        for char in s:
            count_map[char] -= 1

            if char in seen:
                continue
            while result and char < result[-1] and count_map[result[-1]] > 0:
                seen.remove(result.pop())
            result.append(char)
            seen.add(char)

        return "".join(result)

                    

            