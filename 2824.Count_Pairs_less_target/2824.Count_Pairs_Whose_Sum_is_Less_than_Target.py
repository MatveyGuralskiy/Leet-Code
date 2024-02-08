#--------------LEET CODE---------------
#2824. Count Pairs Whose Sum is Less than Target

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count=0
        for a in range(len(nums)):
            for i in range(a+1,len(nums)):
                if nums[a]+nums[i]<target:
                    count+=1
        return count