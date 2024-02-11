#--------------LEET CODE---------------
#2427. Number of Common Factors

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
"""
2427. Number of Common Factors
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.

 

Example 1:

Input: a = 12, b = 6
Output: 4
Explanation: The common factors of 12 and 6 are 1, 2, 3, 6.

Example 2:

Input: a = 25, b = 30
Output: 2
Explanation: The common factors of 25 and 30 are 1, 5.
 

Constraints:

1 <= a, b <= 1000
"""

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
    
