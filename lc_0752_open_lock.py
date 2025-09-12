from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = "0000"
        if target == start:
            return 0
        deads = set(deadends)
        if start in deads:
            return -1
        seen = set()

        def generate_nexts(current):
            nexts = []
            for i in range(4):
                higher_str = (
                    current[0:i]
                    + (str(int(current[i]) + 1) if int(current[i]) < 9 else "0")
                    + current[i + 1 :]
                )  # TODO: verify that this doesn't error at ends
                if higher_str not in deads and higher_str not in seen:
                    nexts.append(higher_str)
                    seen.add(higher_str)
                    if higher_str == target:
                        return nexts, True
                lower_str = (
                    current[0:i]
                    + (str(int(current[i]) - 1) if int(current[i]) > 0 else "9")
                    + current[i + 1 :]
                )
                if lower_str not in deads and lower_str not in seen:
                    nexts.append(lower_str)
                    seen.add(lower_str)
                    if lower_str == target:
                        return nexts, True
            return nexts, False

        count, nexts = 0, [start]
        while nexts != []:
            count, next_nexts = count + 1, []
            for elem in nexts:
                level_search, found = generate_nexts(elem)
                if found:
                    return count
                next_nexts = next_nexts + level_search
            nexts = next_nexts
        return -1
