# Last updated: 4/27/2025, 11:14:15 PM
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and asteroid < 0 < stack[-1]: # ignore negative asteroids at the start of the stack
                if stack[-1] < -asteroid:
                    stack.pop()  # smaller one explodes, continue
                elif stack[-1] == -asteroid:
                    stack.pop()  # both explode
                    break
                else:
                    break  # incoming one explodes
            else:
                stack.append(asteroid)

        return stack

'''
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
                continue

            last_dir = -1 if stack[-1] < 0 else 1
            curr_dir = -1 if asteroid < 0 else 1

            if last_dir == curr_dir or (last_dir == -1 and curr_dir == 1):
                print(asteroid)
                stack.append(asteroid)
                continue

            while last_dir != curr_dir:                    
                last_asteroid = stack.pop()

                if abs(last_asteroid) > abs(asteroid):
                    asteroid = last_asteroid
                    break
                elif abs(last_asteroid) == abs(asteroid):
                    asteroid = None
                    break
                elif not stack:
                    break
                else:
                    last_dir = -1 if stack[-1] < 0 else 1

            if asteroid != None:
                stack.append(asteroid)

        return stack
'''