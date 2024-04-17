//--------------LEET CODE---------------
//2160. Minimum Sum of Four Digit Number After Splitting Digits

//Solution of Matvey Guralskiy
//https://github.com/MatveyGuralskiy
/*
You are given a positive integer num consisting of exactly four digits. Split num into two new integers new1 and new2 by using the digits found in num. Leading zeros are allowed in new1 and new2, and all the digits found in num must be used.

For example, given num = 2932, you have the following digits: two 2's, one 9 and one 3. Some of the possible pairs [new1, new2] are [22, 93], [23, 92], [223, 9] and [2, 329].
Return the minimum possible sum of new1 and new2.

 

Example 1:

Input: num = 2932
Output: 52
Explanation: Some possible pairs [new1, new2] are [29, 23], [223, 9], etc.
The minimum sum can be obtained by the pair [29, 23]: 29 + 23 = 52.
Example 2:

Input: num = 4009
Output: 13
Explanation: Some possible pairs [new1, new2] are [0, 49], [490, 0], etc. 
The minimum sum can be obtained by the pair [4, 9]: 4 + 9 = 13.
 

Constraints:

1000 <= num <= 9999
*/
var minimumSum = function (num) {
    let arr = [];
    while (num > 0) {
        arr.push(num % 10);
        // Update num to remove the last digit
        num = Math.floor(num / 10);
    }
    arr.sort();
    let i = 0;
    let num1 = [];
    let num2 = [];
    while (i < arr.length) {
        if (i % 2 === 0) {
            num1.push(arr[i]);
        } else {
            num2.push(arr[i]);
        }
        i++;
    };
    // remove spaces and last digits with dot
    return parseInt(num1.join('')) + parseInt(num2.join(''));
};