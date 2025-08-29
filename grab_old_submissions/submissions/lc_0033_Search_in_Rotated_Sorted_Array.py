class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return 0 if nums[0]==target else -1
        L, R = 0,len(nums)-1
        while L<R:
            middle = (R+L)//2
            # Standard cases
            if target>=nums[L]:
                if target<=nums[middle] or nums[middle]<nums[L]:
                    R = middle
                else:
                    L = middle+1
            else:
                if target>nums[middle] or nums[middle]>nums[R]:
                    L = middle+1
                else:
                    R = middle
            if target == nums[L]:
                return L
            if target == nums[R]:
                return R
        return -1