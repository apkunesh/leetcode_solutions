/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} m
 * @return {number}
 */

var maxSum = function (nums, k, m) {
  /**
   * NOTE: Basic idea here is to create k windows of (at least) size m while keeping out as many negative numbers as possible. We still want to allow windows containing neg nums (but whose sum is positive) to contribute.
   * This is almost certain to be DP-based.
   * Perhaps something like "Given starting index i and windows k, what is the max sum?"
   */
  let cache = Map();
  // Will use starting index and k windows
  let prefixSum = [nums[0]];
  for (i = 1; i < nums.length; i++) {
    prefixSum.push(prefixSum[i - 1] + nums[i]);
  }
};

console.log(maxSum([1, 2, -1, 3, 3, 4], 2, 2)); // 13
console.log(maxSum([-10, 3, -1, -2], 4, 1)); // -10
