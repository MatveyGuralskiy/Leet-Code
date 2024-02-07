#--------------LEET CODE---------------
#1. Two Sum

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for a in range(n - 1):
            for i in range(a + 1, n):
                if nums[a] + nums[i] == target:
                    return [a, i]
        return []