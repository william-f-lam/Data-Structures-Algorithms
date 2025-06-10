# Leetcode #238

# Prompt:

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Solution:

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    # Creating the prefix and suffix arrays with the exact amount of slots.
    prefix = [0] * n
    suffix = [0] * n
    # Setting the multipliers at 1.
    l_mult = 1
    r_mult = 1

    for i in range(n):
      # j will start at the last element and count down.
      j = -i - 1
      # Set the array as the product of the prior elements.
      prefix[i] = l_mult
      suffix[j] = r_mult
      # Update the multipliers.
      l_mult *= nums[i]
      r_mult *= nums[j]
    # Return the two arrays multiplied by each other.
    return [pre * suf for pre, suf in zip(prefix, suffix)]
    
