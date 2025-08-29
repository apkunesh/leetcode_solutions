def helper(nums,k,index,cur_arr,results):
    if len(cur_arr) == k:
        results.append(cur_arr.copy())
        return
    if index == len(nums):
        return
    cur_arr.append(nums[index])
    helper(nums,k,index+1,cur_arr,results)
    cur_arr.pop()
    helper(nums,k,index+1,cur_arr,results)

def create_n_choose_k(n,k):
    base_nums = [i for i in range(n)]
    results = []
    helper(base_nums,k,0,[],results)
    return results

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        num_to_count = {}
        for num in nums:
            num_to_count[num] = 1 if num_to_count.get(num) is None else num_to_count[num]+1
        results = [[]]
        for num_key in list(num_to_count.keys()):
            new_result = []
            for prev_result in results:
                input_positions = create_n_choose_k(len(prev_result)+num_to_count[num_key],num_to_count[num_key])
                for input_position in input_positions:
                    dummy = prev_result.copy()
                    for input_choice in input_position:
                        dummy.insert(input_choice,num_key)
                    new_result.append(dummy.copy())
            results = new_result
        return results