# LeetCode #2239 

# Prompt: Given an integer array nums of size n, return the number with the value closest to 0 in nums. 
# If there are multiple answers, return the number with the largest value.

# Solution:

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Start with the first index; constraint grants at least 1 item.
        closest = nums[0]
        # Iterate through remaining numbers.
        for num in nums:
            # Compare absolute minimum value for closes to zero.
            if abs(num) < abs(closest):
                closest = num
        # Check the edge case that there are multiple answers, and return the larger number.
        if closest < 0 and abs(closest) in nums:
            # Edge case is true in this case.
            return abs(closest)
        else:
            return closest

        # Time complexity of O(n), due to two separate iterating loops.
        # Space complexity of O(1), constant since we do not need any storage.
