#--------------LEET CODE---------------
#136. Single Number

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        Count={}
        for num in nums:
            Count[num]=Count.get(num,0)+1
        for key,value in Count.items():
            if value==1:
                return key