# Leetcode #392

# Prompt: Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# Answer:

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # I need a counter which will go until the length of t.
        count = 0
        subSize = len(s)

        # Check for empty strings.
        if subSize != 0 and len(t) != 0:
            for index, char in enumerate(t):
                # I'm looping through t to check incrementally if each s char is present.
                if count + 1 <= len(s) and t[index] == s[count]:
                    count += 1
            # The loop only increments if it's in the right order, just delete extras.
        return count >= subSize

# Time Complexity: O(n)
# Space Complexity: O(1)
