#--------------LEET CODE---------------
#509. Fibonacci Number

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        elif n==3:
            return 2
        elif n==4:
            return 3
        else:
            return (self.fib(n-1)+self.fib(n-2))