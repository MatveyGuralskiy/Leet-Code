//--------------LEET CODE---------------
//876. Middle of the Linked List

//Solution of Matvey Guralskiy
//https://github.com/MatveyGuralskiy

/*
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 
*/

var middleNode = function(head) {
    let slow = head;
    let fast = head;

    //slow moves one element
    //fast moves two elements
    //when fast equal to null it means that slow is the middle of array
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }

    return slow;
};