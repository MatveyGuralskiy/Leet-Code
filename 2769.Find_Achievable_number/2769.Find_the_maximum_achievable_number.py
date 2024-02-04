#--------------LEET CODE---------------
#2769. Find the maximum achievable number

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num+2*t

num=4
t=2

FINALLYSOLUTION=Solution()
RESULT=FINALLYSOLUTION.theMaximumAchievableX(num,t)
print(f"The Maximum Achievable number X for {num} and {t} is {RESULT}")