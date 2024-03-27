//--------------LEET CODE---------------
//2622. Cache With Time Limit

//Solution of Matvey Guralskiy
//https://github.com/MatveyGuralskiy
/*
Write a class that allows getting and setting key-value pairs, however a time until expiration is associated with each key.

The class has three public methods:

set(key, value, duration): accepts an integer key, an integer value, and a duration in milliseconds. Once the duration has elapsed, the key should be inaccessible. The method should return true if the same un-expired key already exists and false otherwise. Both the value and duration should be overwritten if the key already exists.

get(key): if an un-expired key exists, it should return the associated value. Otherwise it should return -1.

count(): returns the count of un-expired keys.

 

Example 1:

Input: 
actions = ["TimeLimitedCache", "set", "get", "count", "get"]
values = [[], [1, 42, 100], [1], [], [1]]
timeDelays = [0, 0, 50, 50, 150]
Output: [null, false, 42, 1, -1]
Explanation:
At t=0, the cache is constructed.
At t=0, a key-value pair (1: 42) is added with a time limit of 100ms. The value doesn't exist so false is returned.
At t=50, key=1 is requested and the value of 42 is returned.
At t=50, count() is called and there is one active key in the cache.
At t=100, key=1 expires.
At t=150, get(1) is called but -1 is returned because the cache is empty.
Example 2:

Input: 
actions = ["TimeLimitedCache", "set", "set", "get", "get", "get", "count"]
values = [[], [1, 42, 50], [1, 50, 100], [1], [1], [1], []]
timeDelays = [0, 0, 40, 50, 120, 200, 250]
Output: [null, false, true, 50, 50, -1, 0]
Explanation:
At t=0, the cache is constructed.
At t=0, a key-value pair (1: 42) is added with a time limit of 50ms. The value doesn't exist so false is returned.
At t=40, a key-value pair (1: 50) is added with a time limit of 100ms. A non-expired value already existed so true is returned and the old value was overwritten.
At t=50, get(1) is called which returned 50.
At t=120, get(1) is called which returned 50.
At t=140, key=1 expires.
At t=200, get(1) is called but the cache is empty so -1 is returned.
At t=250, count() returns 0 because the cache is empty.
 

Constraints:

0 <= key, value <= 109
0 <= duration <= 1000
1 <= actions.length <= 100
actions.length === values.length
actions.length === timeDelays.length
0 <= timeDelays[i] <= 1450
actions[i] is one of "TimeLimitedCache", "set", "get" and "count"
First action is always "TimeLimitedCache" and must be executed immediately, with a 0-millisecond delay
*/
// Define the TimeLimitedCache class
var TimeLimitedCache = function () {
    // Initialize an empty cache object
    this.cache = {};
};

// Method to set a key-value pair in the cache with a specified duration
TimeLimitedCache.prototype.set = function (key, value, duration) {
    // If the key already exists in the cache and has a timer set
    if (this.cache[key] && this.cache[key].timer) {
        // Clear the existing timer associated with the key
        clearTimeout(this.cache[key].timer);
        // Update the value associated with the key
        this.cache[key].value = value;
        // Set a new timer for the key with the specified duration
        this.cache[key].timer = setTimeout(() => {
            // When the duration expires, remove the key from the cache
            this.remove(key);
        }, duration);
        // Return true indicating that the value has been updated
        return true;
    } else {
        // If the key doesn't exist in the cache or has no timer set
        // Create a new entry in the cache for the key with the specified value and timer
        this.cache[key] = {
            value: value,
            timer: setTimeout(() => {
                // When the duration expires, remove the key from the cache
                this.remove(key);
            }, duration)
        };
        // Return false indicating that a new entry has been added to the cache
        return false;
    }
};

// Method to get the value associated with a given key from the cache
TimeLimitedCache.prototype.get = function (key) {
    // If the key exists in the cache and has a timer set
    if (this.cache[key] && this.cache[key].timer) {
        // Return the value associated with the key
        return this.cache[key].value;
    } else {
        // If the key doesn't exist in the cache or has no timer set, return -1
        return -1;
    }
};

// Method to count the number of active entries in the cache
TimeLimitedCache.prototype.count = function () {
    let count = 0;
    // Iterate through the cache object and count entries with active timers
    for (const key in this.cache) {
        if (this.cache[key].timer) {
            count++;
        }
    }
    // Return the count of active entries
    return count;
};

// Method to remove a key-value pair from the cache
TimeLimitedCache.prototype.remove = function (key) {
    // Remove the key from the cache object
    delete this.cache[key];
};