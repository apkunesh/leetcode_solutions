from typing import List


class Solution:
    def kSmallestPairs(
        self, nums1: List[int], nums2: List[int], k: int
    ) -> List[List[int]]:
        p1, p2 = 1, 1
        result = [[nums1[0], nums2[0]]]
        while len(result) < k:
            left = nums1[p1] if p1 < len(nums1) else 10**10
            right = nums2[p2] if p2 < len(nums2) else 10**10
            if left < right:
                for i in range(p2):
                    result.append([nums1[p1], nums2[i]])
                    if len(result) == k or nums1[p1] + nums2[i] > nums1[0] + nums2[p2]:
                        break
                p1 += 1
            else:
                for i in range(p1):
                    result.append([nums1[i], nums2[p2]])
                    if len(result) == k or nums2[p2] + nums1[i] > nums2[0] + nums1[p1]:
                        break
                p2 += 1

        _ = k, nums1, nums2
        return result


soln = Solution().kSmallestPairs
print(f"{soln([1,7,11],[2,4,6],3)} should be [[1,2],[1,4],[1,6]]")
print(f"{soln([1,1,2],[1,2,3],2)} should be [[1,1],[1,1]]")
