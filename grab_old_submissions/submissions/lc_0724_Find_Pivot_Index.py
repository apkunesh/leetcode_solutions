class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        if nums[-1]-nums[0] == 0:
            return 0
        for i in range(1,len(nums)):
            if nums[i-1] == nums[-1]-nums[i]:
                return i
        return -1 