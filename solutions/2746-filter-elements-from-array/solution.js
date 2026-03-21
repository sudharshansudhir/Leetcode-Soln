/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    new_arr=arr.filter((no,i)=>fn(no,i))
    return new_arr
};
