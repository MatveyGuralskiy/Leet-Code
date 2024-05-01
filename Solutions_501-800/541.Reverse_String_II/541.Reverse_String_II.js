//--------------LEET CODE---------------
//541. Reverse String II

//Solution of Matvey Guralskiy
//https://github.com/MatveyGuralskiy
/*
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
*/
var reverseStr = function (s, k) {
    if (k > s.length) return s.split('').reverse().join('');
    const split = s.split('');
    // reverse the segment and put it back
    for (let i = 0; i < s.length; i += 2 * k) {
        const reverse = split.splice(i, k).reverse();
        split.splice(i, 0, ...reverse);
    }
    return split.join('');
};