#--------------LEET CODE---------------
#387. First Unique Character in a String

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
"""

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = Counter(s)
        for a,i in l.items():
            if i==1:
                return s.index(a)
        return -1