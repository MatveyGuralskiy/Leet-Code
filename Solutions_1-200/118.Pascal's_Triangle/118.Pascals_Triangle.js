//--------------LEET CODE---------------
//118. Pascal's Triangle

//Solution of Matvey Guralskiy
//https://github.com/MatveyGuralskiy
/*
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
*/
var generate = function (numRows) {
    // new array
    let triangle = [];
    // if triangle doesn't exist
    if (numRows === 0) {
        return triangle;
    }
    // first row always equal 1
    triangle.push([1]);
    // loop check the rest off rows in triangle
    for (let i = 1; i < numRows; i++) {
        // we need previous row to work with it
        let prevRow = triangle[i - 1];
        // new row always started with 1
        let newRow = [1];
        // loop check all rows instead the first and last
        for (let j = 1; j < prevRow.length; j++) {
            newRow.push(prevRow[j - 1] + prevRow[j]);
        }
        // we add the last row 1
        newRow.push(1);
        // add to the array
        triangle.push(newRow);
    }
    return triangle;
};