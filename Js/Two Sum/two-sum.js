/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var dict= {}

    for(let i = 0; i<nums.length; i++) {
        let inp = nums[i],
            diff = target-inp;
        if(diff in dict)
            return [dict[diff], i]
    
        dict[inp] = i;
    }

    return null;

};