class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        duplicates = {}
        for i in range(len(nums)):
            if num_to_index.get(nums[i]) == None:
                num_to_index[nums[i]] = i
            else:
                duplicates[nums[i]] = i
        for i in range(len(nums)):
            cur = nums[i]
            remainder = target - nums[i]
            other_index = num_to_index.get(remainder)
            if (other_index is not None) and (other_index != i):
                return [i,other_index]
            if (other_index is not None) and (other_index == i):
                possible_dupe = duplicates.get(remainder)
                if possible_dupe:
                    return [i,possible_dupe]
            