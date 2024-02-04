#--------------LEET CODE---------------
#69.Sqrt(x)

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(x**0.5)
FINALLY=Solution()
Result=FINALLY.mySqrt(144)
print(Result)