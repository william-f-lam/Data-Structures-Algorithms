# Leetcode #13

# Prompt: Convert a string of Roman numerals to an integer.

# Solution:

class Solution:
    def romanToInt(self, s: str) -> int:
        # Initialize a dictionary of numeral/value pairs to compare later.
        values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M': 1000}
        sum = 0
        stringLen = len(s)

        # Similar to a C++ for loop, but increment depends on situation.
        i = 0
        while i < stringLen:
            # In the case of a subtractive numeral, make sure following value is larger.
            # Also protect against edge case of last numeral, check this first.
            if ((i + 1) < stringLen) and (values[s[i]] < values[s[i + 1]]):
                sum += values[s[i + 1]] - values[s[i]]
                # Increment two because account for the value of both the current and next.
                i += 2
            else:
                # Add normally in all other cases.
                sum += values[s[i]]
                i +=1
        return sum

    # Time complexity of O(n) based on one iteration through the string.
    # Space complexity of O(1) due to constant storage.
        
