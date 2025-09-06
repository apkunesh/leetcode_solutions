from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0 and len(nums2) == 0:
            return 0
        if len(nums1) == 0:
            if len(nums2) == 1:
                return nums2[0]
            return (
                nums2[len(nums2) // 2]
                if len(nums2) % 2 == 1
                else (nums2[len(nums2) // 2] + nums2[len(nums2) // 2 - 1]) / 2
            )
        if len(nums2) == 0:
            if len(nums1) == 1:
                return nums1[0]
            return (
                nums1[len(nums1) // 2]
                if len(nums1) % 2 == 1
                else (nums1[len(nums1) // 2] + nums1[len(nums1) // 2 - 1]) / 2
            )
        longer = nums1 if len(nums1) > len(nums2) else nums2
        shorter = nums2 if len(nums1) > len(nums2) else nums1
        total = len(longer) + len(shorter)
        L = 0
        R = len(shorter)
        required_elements = total // 2 + 1
        candidate = (L + R) // 2
        longer_elements = required_elements - candidate
        # How do we know if candidate is correct?
        # Well, the element in the longer list has to be less than the right of the shorter and bigger than the left of the shorter.
        # Similarly, the element in the shorter list has to be less than the right of the longer and bigger than the left of the longer.
        # How to handle OOB cases? These should be automatically true, most likely.
        smaller_index = candidate - 1
        larger_index = longer_elements - 1
        condition_1 = (
            shorter[smaller_index] >= longer[larger_index - 1]
            if larger_index - 1 >= 0
            else True
        )  # If not this, then we need to go right
        condition_2 = (
            shorter[smaller_index] <= longer[larger_index + 1]
            if larger_index + 1 < len(longer)
            else True
        )  # If not this, then we need to go left
        condition_3 = (
            longer[larger_index] >= shorter[smaller_index - 1]
            if smaller_index - 1 >= 0
            else True
        )  # If not this, then we need to go left
        condition_4 = (
            longer[larger_index] <= shorter[smaller_index + 1]
            if smaller_index + 1 < len(shorter)
            else True
        )  # If not this, then we need to go right
        while not all([condition_1, condition_2, condition_3, condition_4]):
            if not condition_1 or not condition_4:
                L = candidate + 1
            elif not condition_2 or not condition_3:
                R = candidate - 1
            candidate = (L + R) // 2
            longer_elements = required_elements - candidate
            smaller_index = candidate - 1
            larger_index = longer_elements - 1
            condition_1 = (
                shorter[smaller_index] >= longer[larger_index - 1]
                if larger_index - 1 >= 0
                else True
            )  # If not this, then we need to go right
            condition_2 = (
                shorter[smaller_index] <= longer[larger_index + 1]
                if larger_index + 1 < len(longer)
                else True
            )  # If not this, then we need to go left
            condition_3 = (
                longer[larger_index] >= shorter[smaller_index - 1]
                if smaller_index - 1 >= 0
                else True
            )  # If not this, then we need to go left
            condition_4 = (
                longer[larger_index] <= shorter[smaller_index + 1]
                if smaller_index + 1 < len(shorter)
                else True
            )  # If not this, then we need to go right
        # Okay, so now we have the correct number of elements to include. Let's consider the two edge cases, then do the general case
        print(candidate)
        if candidate == 0:
            if total % 2 == 1:
                return longer[larger_index]
            else:
                return (longer[larger_index] + longer[larger_index - 1]) / 2
        elif candidate == len(shorter):
            print("in here")
            if total % 2 == 1:
                return (
                    max([shorter[-1], longer[larger_index]])
                    if larger_index >= 0
                    else shorter[-1]
                )
            else:
                candidate_elements = [shorter[-1], longer[larger_index]]
                if larger_index > 0:
                    candidate_elements.append(longer[larger_index - 1])
                    candidate_elements.sort()
                return (candidate_elements[-1] + candidate_elements[-2]) / 2
        if total % 2 == 1:
            return max([shorter[smaller_index], longer[larger_index]])
        else:
            candidate_elements = [
                shorter[smaller_index],
                shorter[smaller_index - 1],
                longer[larger_index - 1],
                longer[larger_index],
            ]
            candidate_elements.sort()
            return (candidate_elements[-1] + candidate_elements[-2]) / 2
