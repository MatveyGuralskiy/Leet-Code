//--------------LEET CODE---------------
//2705. Compact Object

//Solution of Matvey Guralskiy
//https://github.com/MatveyGuralskiy
/*
Given an object or array obj, return a compact object. A compact object is the same as the original object, except with keys containing falsy values removed. This operation applies to the object and any nested objects. Arrays are considered objects where the indices are keys. A value is considered falsy when Boolean(value) returns false.

You may assume the obj is the output of JSON.parse. In other words, it is valid JSON.

 

Example 1:

Input: obj = [null, 0, false, 1]
Output: [1]
Explanation: All falsy values have been removed from the array.
Example 2:

Input: obj = {"a": null, "b": [false, 1]}
Output: {"b": [1]}
Explanation: obj["a"] and obj["b"][0] had falsy values and were removed.
Example 3:

Input: obj = [null, 0, 5, [0], [false, 16]]
Output: [5, [], [16]]
Explanation: obj[0], obj[1], obj[3][0], and obj[4][0] were falsy and removed.
 
*/
var compactObject = function (obj) {
    if (obj === null || typeof obj !== "object") {
        return obj;
    };
    // check if object is array
    if (Array.isArray(obj)) {
        // object will filtered by Boolen and will delete all types of: "null, undefined and false"
        // we will recursive the function and map will work with every element
        return obj.filter(Boolean).map(compactObject);
    };
    // if the element isn't defined as an array so it's object 
    const result = {};
    for (const key in obj) {
        let value = compactObject(obj[key]);
        // if the result of element is correct we will add him to our object 'result'
        if (value) result[key] = value;
    }
    return result;
};