# Leetcode #14

# Prompt: Write a function to find the longest common prefix string amongst an array of strings.
#         If there is no common prefix, return an empty string "".

# Answer:

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # To avoid going out of bounds, we need to find the length of the smallest string.
        minLen = float('inf')
        for s in strs:
            if len(s) < minLen:
                minLen = len(s)
        i = 0
        while i < minLen:
            # We need to iterate through the strings to check their prefix.
            for s in strs:
                # The moment a string doesn't match the first string's prefix, enter the conditional.
                if s[i] != strs[0][i]:
                    # Return the first string just up to before the ith index.
                    return strs[0][:i]
            i += 1
        return strs[0][:i]
