# Leetcode #228

# Prompt: You are given a sorted unique integer array nums.
#         A range [a,b] is the set of all integers from a to b (inclusive).
#         Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
#         That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

# Solution:

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []
        if len(nums) != 0:
            leftRange = 0
        else:
            return ranges
        # First thought is that I'll need to iterate through the array.
        for index, num in enumerate(nums):
            # Now I need to check for disconnects to restart the range. 
            if index == 0:
                continue
            if (num - 1) != nums[index - 1]:
                if (nums[leftRange] == nums[index - 1]):
                    ranges.append(str(nums[leftRange]))
                else:
                    ranges.append(f"{nums[leftRange]}->{nums[index - 1]}")
                leftRange = index
        # Also need to include the last number/range if continuous
        if (nums[leftRange] == nums[len(nums) - 1]):
            ranges.append(str(nums[leftRange]))
        else:
            ranges.append(f"{nums[leftRange]}->{nums[len(nums) - 1]}")
        return ranges
  # Time: O(n)
  # Space: O(n)
