#--------------LEET CODE---------------
#13. Roman to Integer

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
class Solution:
    def romanToInt(self, s: str) -> int:
        Dict={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        ans = 0
        prev_value = 0

        for char in s:
            value = Dict[char]
            if prev_value < value:
                ans += value - 2 * prev_value
            else:
                ans += value
            prev_value = value

        return ans