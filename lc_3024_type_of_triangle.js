/**
 * @param {number[]} nums
 * @return {string}
 */

var intCompare = function (a, b) {
  return a - b;
};

var triangleType = function (nums) {
  nums = nums.sort(intCompare);
  if (nums[0] + nums[1] <= nums[2]) {
    return "none";
  }
  if (nums[0] === nums[1] && nums[1] === nums[2]) {
    return "equilateral";
  } else if (
    nums[0] === nums[1] ||
    nums[1] === nums[2] ||
    nums[2] === nums[0]
  ) {
    return "isosceles";
  } else {
    return "scalene";
  }
};

console.log(triangleType([5, 3, 8]));
console.log(triangleType([10, 4, 6]));
