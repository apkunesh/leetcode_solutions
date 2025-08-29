from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # nlogn
        seen = set()
        two_sum = defaultdict(set) # Map from sum to sets of sorted nums.
        three_sum = set()
        for num in nums:
            # Further optimization: if I've seen a number 3 times, I don't think I need to consider it anymore.
            if -num in two_sum:
                for combination in two_sum[-num]: # set of tuple
                    three_sum.add((combination[0],combination[1],num))
            if num in seen:
                two_sum[num+num].add((num,num))
            else:
                for elem in seen: # n^2
                    two_sum[elem+num].add((elem,num))
                    # Optimization: add a "seen" for tuples?
            seen.add(num)
        return [list(elem) for elem in three_sum]