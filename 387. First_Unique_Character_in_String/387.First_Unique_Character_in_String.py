#--------------LEET CODE---------------
#387. First Unique Character in a String

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy

from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = Counter(s)
        for a,i in l.items():
            if i==1:
                return s.index(a)
        return -1