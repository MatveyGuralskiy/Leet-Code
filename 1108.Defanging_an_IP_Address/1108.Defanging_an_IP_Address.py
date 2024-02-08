#--------------LEET CODE---------------
#1108. Defanging an IP Address

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
    
#S=Solution()
#print(S.defangIPaddr('1.1.1.1'))