class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        # Did not consider edge case of k=0.
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k==0: return False
        window_set = set()
        for i in range(len(nums)):
            if nums[i] in window_set:
                return True
            if (i-k) >= 0:
                window_set.remove(nums[i-k])
            window_set.add(nums[i])
        return False