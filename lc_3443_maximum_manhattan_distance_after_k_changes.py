from collections import defaultdict


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        """
        This one is deceptive. A few thoughts:
        (1) Any given movement changes the local manhattan distance by 1.
        (2) We can determine majority directions in O(n) time.
        (3) The global movement is the optimum of the local movements.
        (4) Greedy without majority seems bad. For example, consider NNSSS, k=2. Greedily switching S to N will result in max length of 4 even though switching both Ns to Ss would result in a max dist of 5.
        Maybe thinking in ranges will help?
        How about this:
        At each level, we compute the local manhatten distance, knowing both the # of
        Ns and # of Ss (and Es and Ws) present. Theh max after changes can now be determined by taking the larger of each pair and "flipping" two of the smaller. Doing this across the whole array *should* yield the max possible.
        """
        char_count = defaultdict(int)
        result = 0
        x, y = 0, 0
        for char in s:
            char_count[char] += 1
            if char == "N":
                y += 1
            elif char == "S":
                y -= 1
            elif char == "W":
                x -= 1
            elif char == "E":
                x += 1
            else:
                raise Exception()
            m_dist = abs(x) + abs(y)
            # print(f"Current mdist: {m_dist}")
            north_south_diff = min(char_count["S"], char_count["N"])
            east_west_diff = min(char_count["E"], char_count["W"])
            ns_changes = min([k, north_south_diff])
            ew_changes = min([k - ns_changes, east_west_diff])
            # print(f"Possible changes NS are {ns_changes}, EW are {ew_changes}")
            modified_m_dist = m_dist + 2 * ns_changes + 2 * ew_changes
            result = max(result, modified_m_dist)
            # print(result)
        return result


soln = Solution().maxDistance
print(f"{soln("NSWWEW",3)} should be 6")
print(f"{soln("NWSE",1)} should be 3")
