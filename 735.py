from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # We track the asteroids in a stack. If we encounter a negative asteroid, we check the top of the stack.
        # If the top of the stack is positive, we compare the absolute values and decide whether to pop or keep the asteroid.
        # Time complexity, O(n) : We iterate through the list once
        # Space complexity, O(n) : In the worst case, we store all asteroids in the stack
        # Performance: 
        # Runtime: faster than 93.56%
        # Memory Usage: less than 20.19%.
        stack= [asteroids[0]]
        for asteroid in asteroids[1:]:
            if asteroid < 0:      
                while True:
                    if len(stack) == 0:
                        stack.append(asteroid)
                        break
                    elif stack[-1] > abs(asteroid):
                        break
                    elif stack[-1] == abs(asteroid):
                        stack.pop()
                        break
                    elif stack[-1] > 0 and abs(asteroid) > stack[-1]:
                        stack.pop()
                    else:
                        stack.append(asteroid)
                        break
            else:
                stack.append(asteroid)
        return stack