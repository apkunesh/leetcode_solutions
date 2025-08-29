def scan(res_list, nums, left_first,right_first):
    for i in range(1, len(nums)):
        if i == len(nums) - 1:
            if left_first is True:
                res_list.append(res_list[-1])
                continue
        left, right = res_list[-2] + nums[i], res_list[-1]
        dummy = left_first
        left_first = right_first
        if left > right:
            res_list.append(left)
            right_first = dummy
        elif left < right:
            res_list.append(right)
            right_first = right_first
        else:
            res_list.append(right)
            if (
                right_first is False
                or dummy is False
            ):
                right_first = False
            else:
                right_first = True
    return res_list[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left_includes_first,res_list= False,[0, nums[0]]
        f1 = scan(res_list, nums, False, True)
        nums_2 = nums.copy()
        nums_2.append(nums[0])
        nums_2 = nums_2[1:]
        second_result = [0, nums_2[0]]
        f2 = scan(second_result, nums_2,False, True)
        return max(f1, f2)
