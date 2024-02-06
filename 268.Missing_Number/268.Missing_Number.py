#--------------LEET CODE---------------
#268. Missing Number

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)
    