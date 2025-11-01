/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var intComparison = function (a, b) {
  return b - a;
};

var minOperations = function (nums, k) {
  /**
   * NOTE: It's not at all intuitive to me how to do this without direct construction, as the element we add (equivalent to min + 2*avg)
   * It should be bounded from below by n/2 where n is the number of elements less than k.
   *
   */
  nums.sort(intComparison);
  let firstNum = 0;
  let secondNum = 0;
  let newQueue = [];
  let count = 0;
  // Enqueue with push, dequeue with shift
  // console.log(nums);
  // console.log(nums[nums.length - 1]);
  while (
    (newQueue.length > 0 && newQueue[0] < k) ||
    (nums.length > 0 && nums[nums.length - 1] < k)
  ) {
    // console.log("INSIDE");
    if (nums.length === 0) {
      firstNum = newQueue.shift();
    } else if (newQueue.length === 0) {
      firstNum = nums.pop();
    } else {
      if (newQueue[0] > nums[nums.length - 1]) {
        firstNum = nums.pop();
      } else {
        firstNum = newQueue.shift();
      }
    }

    if (nums.length === 0) {
      secondNum = newQueue.shift();
    } else if (newQueue.length === 0) {
      secondNum = nums.pop();
    } else {
      if (newQueue[0] > nums[nums.length - 1]) {
        secondNum = nums.pop();
      } else {
        secondNum = newQueue.shift();
      }
    }

    newQueue.push(2 * firstNum + secondNum);
    count++;
  }
  return count;
};

console.log(minOperations([2, 11, 10, 1, 3], 10));
