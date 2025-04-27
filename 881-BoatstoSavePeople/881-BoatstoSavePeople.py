# Last updated: 4/27/2025, 2:52:36 PM
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        start, end = 0, len(people) - 1
        n = 0

        while start < end:
            if people[start] + people[end] > limit:
                n += 1
                end -= 1
            elif people[start] + people[end] <= limit:
                n += 1
                start += 1
                end -= 1
        
        if start == end:
            n += 1
        
        return n