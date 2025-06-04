# LeetCode #1768

# Prompt:
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string. Return the merged string.

# Solution:

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Create variables for the lengths of the input words.
        A, B = len(word1), len(word2)
        # Create variables for the counters of a word's letters.
        a, b = 0, 0
        # Store result in a list instead of appending to a string for speed.
        ans = []
        # Indicator for which word to append from.
        word = 1

        # Merge the list as long as either counter does not exceed the word's length.
        while a < A and b < B:
            if word == 1:
                # Append to the list.
                ans.append(word1[a])
                # Increment the counter.
                a += 1
                # Switch to the next word.
                word = 2
            else:
                ans.append(word2[b])
                b += 1
                word = 1

        # Once one word runs out, append the remaining onto the list.
        while a < A:
            ans.append(word1[a])
            a += 1
        while b < B:
            ans.append(word2[b])
            b += 1
        return "".join(ans)

        # Time complexity of O(n), we iterate twice separately.
        # Space complexity of O(n), each letter needs to be stored.
        
