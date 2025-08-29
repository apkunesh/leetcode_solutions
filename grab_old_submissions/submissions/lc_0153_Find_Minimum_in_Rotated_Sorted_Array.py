class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Basic idea: 2 pointer binary search, comparing
        # middle to right. 
        # Note that either the rightmost is the smallest
        # or to the right of the smallest.
        L,R = 0,len(nums)-1
        while L<R:
            M = (L+R)//2
            if nums[M]>nums[R]:
                L=M+1
            else:
                R=M
        return nums[L]