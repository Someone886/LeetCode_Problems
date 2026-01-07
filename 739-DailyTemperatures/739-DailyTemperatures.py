# Last updated: 1/6/2026, 9:53:41 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        # Initialize the result list with 0s. 
4        # This handles the case where no warmer day is found (stays 0).
5        ans = [0] * len(temperatures)
6        
7        # This is our Monotonic Decreasing Stack.
8        # It stores tuples of (temperature, index).
9        records = [] 
10        
11        # Manual counter for the current day's index.
12        day_index = 0
13
14        for temperature in temperatures:
15            # Case 1: Stack is empty OR current temperature is not warmer than the last recorded day.
16            # We simply record this day and move on.
17            if not records or temperature <= records[-1][0]:
18                records.append((temperature, day_index))
19            
20            # Case 2: Current temperature is HOTTER than the day at the top of the stack.
21            else:
22                # We pop ALL days from the stack that are cooler than the current temperature.
23                # This 'while' loop is what allows us to process the 'Next Greater Element'.
24                while records and temperature > records[-1][0]:
25                    # Get the index of the cooler day.
26                    old_temperature, old_day_index = records.pop()
27                    
28                    # Calculate how many days passed between then and now.
29                    ans[old_day_index] = (day_index - old_day_index)
30                
31                # After clearing out cooler days, add current day to the stack.
32                records.append((temperature, day_index))
33            
34            # Increment the day counter for the next iteration.
35            day_index += 1
36
37        return ans