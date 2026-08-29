from typing import List
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        # So for this need to maintain a current max, and then for each question we can either take it or not take it, if we take it we need to skip the next questions[idx][1] questions, if we don't take it we just move to the next question.
        # Time complexity: O(n), where n is the length of the questions list, we
        # visit each element once.
        # Space complexity: O(n), we are using a list to store the maximum points that
        # can be earned from each question.
        # Performance:
        # Runtime: faster than 78.14%.
        # Memory Usage: less than 66.70%.
        # 2, 5
        current = [0] * (len(questions) + 1)
        max_curr = 0
        for idx in range(len(questions) -1, -1, -1):
            if 1 + idx + questions[idx][1] < len(questions):
                current[idx] = max(current[idx + 1], questions[idx][0] + current[1 + idx + questions[idx][1]])
            else:
                current[idx] = max(questions[idx][0], current[idx + 1])
        return current[0]