from math import ceil, log10
from typing import Dict


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        """
        Goal here is to find the smallest number strictly greater than n where, for each present numeral "a", there are "a" instances of that numeral in the result.
        For example, 20 -> 22; 0 -> 1; 100 -> 122; 200 -> 212; 220 -> 221
        Also, 1000 -> 1333; 1334 -> 3133; 4000 -> 4444
        Interesting to notice that we sorta bootstrap the next one off the previous one. Let's try enumerating.
        [0,0] -> 1; [1,21] -> 22; [22,121] -> 122; [122,211] -> 212; [212,220] -> 221; [220,1332] -> 1333; [1333,3132]-> 3133; [3133,3312]-> 3313; [3313,3330]-> 3331
        Now we get to something really interesting.
        14444 22333 23233 23323 23332 32233 32323 32332 33223 33232 33322 41444 44144 44414 44441 55555
        So to firm this up a bit, what I'm actually *doing* is taking the unique positive integers which sum to 1, 2, 3, 4, 5 and taking their unique permutations (combinations?)
        Then I'm sorting these and mapping them to ranges. For sufficiently small n (say 10**6) this is trivial. For high orders of magnitude, though, I'd expect that the number of
        "beautiful numbers" becomes unwieldy.
        0 digits -> null
        1 digit -> (1) -> perms of [1]
        2 digits -> (2) -> perms of [2,2]
        3 digits -> (2,1) (3) -> perms of [1,2,2] and [3,3,3]
        4 digits -> (3,1) (4) -> perms of [1,3,3,3] and [4,4,4,4]
        5 digits -> (4,1) (3,2) (5) -> perms of [1,4,4,4,4] and [3,3,3,2,2] and [5,5,5,5,5]
        6 digits -> (5,1) (4,2) (3,2,1) (6) -> perms of [5,5,5,5,5,1] and [4,4,4,4,2,2] and [3,3,3,2,2,1] and [6,6,6,6,6,6]
        7 digits -> (6,1) (5,2) (3,4) (4,2,1) (7) -> perms of [6,6,6,6,6,6,1] and [5,5,5,5,5,2,2] and [3,3,3,4,4,4,4] and [4,4,4,4,2,2,1] and [7,7,7,7,7,7,7]

        TBH this still feels a bit messy, but I think if we construct these up to 1 digit above n's length, then perform binary search, we can find the nearest beatiful number.
        This kicks ass compared to brute-force but still does seem slow to me...
        """

        beautiful_numbers = [1]

        def dfs(num: int, branch_tracker: Dict[int, int], max_digits: int):
            tentative_next = num * 10
            for digit, digit_count in branch_tracker.items():
                if digit_count > 0:
                    branch_tracker[digit] -= 1
                    new_num = tentative_next + digit
                    # print(log10(new_num))
                    if new_num != 0 and ceil(log10(new_num)) == max_digits:
                        beautiful_numbers.append(new_num)
                    else:
                        dfs(new_num, branch_tracker, max_digits)
                    branch_tracker[digit] += 1

        beautiful_number_sets = [
            (1,),
            (2,),
            (2, 1),
            (3,),
            (3, 1),
            (4,),
            (4, 1),
            (3, 2),
            (5,),
            (5, 1),
            (4, 2),
            (3, 2, 1),
            (6,),
            (6, 1),
            (5, 2),
            (3, 4),
            (4, 2, 1),
            (7,),
        ]
        for dig_tuple in beautiful_number_sets:
            total_digits = sum(dig_tuple)
            branch_tracker = {}
            for elem in dig_tuple:
                branch_tracker[elem] = elem
            dfs(0, branch_tracker, total_digits)
        beautiful_numbers.sort()

        l, r = 0, len(beautiful_numbers)
        mid = (l + r) // 2
        while l < r:
            mid = (l + r) // 2
            print(f"Trying {mid}, val {beautiful_numbers[mid]}")
            if beautiful_numbers[mid] > n:
                r = mid
            elif beautiful_numbers[mid] <= n:
                l = mid + 1
            print(f"L and R are now {[l,r]}")
        return beautiful_numbers[l]


soln = Solution().nextBeautifulNumber
print(f"{soln(1)} should be 22")
