# LEETCODE EASY PROBLEM -> https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

from typing import List
nums = [1,2,5] 
target = 7

class Solution:
    # First solution found
    # Runtime: 1642ms   | Beats 33.28%
    # Memory:  17.28 MB | Beats 91.28%
    def twoSum(self, nums: List[int], target: int) -> List[int]: 
        result = [0,0]
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result = [i, j]
                    return result
                
s = Solution()
print(s.twoSum(nums, target))