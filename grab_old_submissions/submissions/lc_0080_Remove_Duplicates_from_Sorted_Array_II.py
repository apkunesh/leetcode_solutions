class Solution(object):
    # Simplified the conditional somewhat and moved on
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Watch for case that L-1 is out-of-bounds left.
        L,R = 0,1
        at_most_2_count = 1
        while R<len(nums):
            if (nums[L] != nums[R]) or (L==0 or nums[L-1]!=nums[L]):
                at_most_2_count += 1
                nums[L+1] = nums[R]
                L += 1
            R+=1
        return at_most_2_count