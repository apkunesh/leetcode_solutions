class NumArray(object):
    # Surprised at the poor memory complexity of the previous. Trying something
    # a little tighter
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]
        self.prefix_sums = nums

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefix_sums[right] - self.prefix_sums[left-1] if left > 0 else self.prefix_sums[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)