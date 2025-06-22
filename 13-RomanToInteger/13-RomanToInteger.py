# Last updated: 6/22/2025, 2:53:37 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        ans = 0
        i = 0
        n = len(s)
        
        while i < n:
            # Value of the current symbol
            current_value = roman_map[s[i]]
            
            # Look ahead to check for subtractive notation (e.g., IV, CM)
            if i + 1 < n:
                next_value = roman_map[s[i+1]]
                if current_value < next_value:
                    # This is a subtractive pair (e.g., I before V for IV)
                    ans += next_value - current_value
                    i += 2  # Move index past both characters
                else:
                    # Not a subtractive pair, just add current value
                    ans += current_value
                    i += 1  # Move index past current character
            else:
                # This is the last character, just add its value
                ans += current_value
                i += 1
                
        return ans