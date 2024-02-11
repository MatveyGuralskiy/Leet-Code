#--------------LEET CODE---------------
#234. Palindrome Linked List

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy
"""
Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.head=head
        data=self.appendList()
        return data==data[::-1]


    def appendList(self):
        nums=list()
        cur=self.head
        while cur:
            nums.append(cur.val)
            cur=cur.next
        return nums