#--------------LEET CODE---------------
#234. Palindrome Linked List

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy

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