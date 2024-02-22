#--------------LEET CODE---------------
#94. Binary Tree Inorder Traversal

#Solution of Matvey Guralskiy
#https://github.com/MatveyGuralskiy

"""
Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

Example 1:


Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]
 

Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
 
"""

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ARRAY = []

        def ITEMS(X) :
            if not X:
                return 
            ITEMS(X.left)
            ARRAY.append(X.val)
            ITEMS(X.right)

        ITEMS(root)
        return ARRAY