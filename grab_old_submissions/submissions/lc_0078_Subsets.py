class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur_set = []
        subsets = []
        self.recurse(0,nums,cur_set,subsets)
        return subsets

    def recurse(self,index,nums,cur_set,subsets):
        if index == len(nums):
            subsets.append(cur_set.copy())
            return

        cur_set.append(nums[index])
        self.recurse(index+1,nums,cur_set,subsets) #Include this val
        cur_set.pop()
        self.recurse(index+1,nums,cur_set,subsets) #Don't include this val    