class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Attempting this with combinations Advanced Algos knowlege.
        result = []
        cur_set = []
        set_sum = [0]
        self.recurse(candidates,cur_set,set_sum,result,target,0)
        return result
    
    def recurse(self,nums,cur_set,set_sum,result,target,index):
        if set_sum[0] > target:
            return
        if set_sum[0] == target:
            result.append(cur_set.copy())
            return
        # sum is less than target
        for i in range(index,len(nums)):
            cur_set.append(nums[i])
            set_sum[0]+=nums[i]
            self.recurse(nums,cur_set,set_sum,result,target,i)
            set_sum[0]-=nums[i]
            cur_set.pop()