#--------------LEET CODE---------------
#169. Majority Element

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for num, count in counts.items():
            if count > majority_count:
                return num
        return -1