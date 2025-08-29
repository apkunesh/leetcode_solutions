class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Basic idea: 0 is our effective "kadane reset". Within each range of nonzeros, we
        # will want to do a pass L to R and R to L, keeping track of the max.
        # This double-sweep should pick up all positive maxes.
        # Gonna do the intuitive way, then can maybe come back and optimize.
        one_beyond_last_zero,grand_max = 0,max(nums) #O(n)
        for i in range(len(nums)+1):
            if i == len(nums) or nums[i]==0:
                # scan right and left
                left_prod,right_prod,count = 1,1,1
                for ind in range(one_beyond_last_zero,i):
                    left_prod = left_prod * nums[ind]
                    right_prod = nums[i-count]*right_prod
                    grand_max = max([grand_max,left_prod,right_prod])
                    count+=1
                one_beyond_last_zero = i+1
        return grand_max