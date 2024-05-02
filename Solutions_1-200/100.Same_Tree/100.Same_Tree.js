//--------------LEET CODE---------------
//100. Same Tree

//Solution of Matvey Guralskiy
//https://github.com/MatveyGuralskiy
/*
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
*/
var isSameTree = function (p, q) {
    if (p == undefined && q == undefined) {
        return true;
    } else if (p == undefined || q == undefined) {
        return false;
        // check if both values the same 
    } else if (p.val != q.val) {
        return false;
    }
    // the answer will be correct only if both sides will be equal
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};