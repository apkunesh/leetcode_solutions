class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Pretty horrific. 
        # First I stumbled through an n^2 soln. 
        # It took like an hour
        # Then I saw Neetcode's expl. up to the point
        # where he mentioned hashmaps, and I was able to get closer to an O(N) soln.
        # The new soln attempted to iterate over keys of the hashmap, which
        # failed for cases ith negatives.
        # Then I made a soln iterating over the prefix sum array, which failed for a similar reason
        # Now, though, I understood that my approach had to do with an intrinsic bias toward
        # positives. The scan over the array worked as long as the sum was never negative,
        # but, once I realized that it needed to handle this case, it became obvious that
        # I should be adding to my total looking only leftward. This avoids double-counting
        # and does not demand that the underlying data be sum-positive.
        if len(nums) == 1:
            return 1 if nums[0] == k else 0
        prefix_sum = nums[0:]
        for i in range(1,len(nums)):
            prefix_sum[i] += prefix_sum[i-1]
        sum_set = {0:1}
        total = 0
        for num in prefix_sum:
            total+=sum_set.get(num-k,0)
            if sum_set.get(num) is None:
                sum_set[num] = 0
            sum_set[num] += 1
        return total