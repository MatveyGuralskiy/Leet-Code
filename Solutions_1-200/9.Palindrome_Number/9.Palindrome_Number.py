#--------------LEET CODE---------------
#9. Palindrome number

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=-14324
        if '0' in str(abs(x)):
            return False
        sign = -1 if x < 0 else 1
        reverse=int(str(abs(x))[::-1])*sign

        if x==reverse:
            return True
S=Solution()
print(S.isPalindrome(121))