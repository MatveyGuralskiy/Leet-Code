#--------------LEET CODE---------------
#2427. Number of Common Factors

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        MINIMAL=min(a,b)
        COUNT=0
        while MINIMAL>0:
            if ( a%MINIMAL==0 and b%MINIMAL==0):
                COUNT+=1
            MINIMAL-=1
        return COUNT

FINALLYSOLUTION=Solution()

a=int(12)
b=int(6)

RESULT=FINALLYSOLUTION.commonFactors(a,b)
print(f"The divided numbers of {a} and {b} is: {RESULT}")
    
