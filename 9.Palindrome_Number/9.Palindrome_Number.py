#--------------LEET CODE---------------
#9. Palindrome number

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
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