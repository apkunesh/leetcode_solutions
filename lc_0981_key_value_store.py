from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.key_to_timestamp_list = defaultdict(list)
        self.tuple_to_value = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_to_timestamp_list[key].append(timestamp)
        self.tuple_to_value[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        timestamp_list = self.key_to_timestamp_list[key]
        L = 0
        R = len(timestamp_list) - 1
        target = (L + R) // 2
        while L <= R:
            target_less = timestamp_list[target] <= timestamp
            right_greater = (
                timestamp_list[target + 1] > timestamp
                if target + 1 < len(timestamp_list)
                else True
            )
            if target_less and right_greater:
                return self.tuple_to_value[(key, timestamp_list[target])]
            if target_less:  # Need to move right
                L = target + 1
            else:
                R = target - 1
            target = (L + R) // 2
        return ""
