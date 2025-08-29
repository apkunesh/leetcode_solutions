class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L,R = 0,1
        uniques = 1
        while R < len(nums):
            if nums[L] != nums[R]:
                uniques +=1
                nums[L+1] = nums[R]
                L+=1
            R += 1
        return uniques
