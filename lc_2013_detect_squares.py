# MISTAKE: Misplaced a paren
from collections import defaultdict
from typing import List


class CountSquares:
    def __init__(self):
        self._x_to_y = defaultdict(set)
        self._point_to_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self._x_to_y[point[0]].add(point[1])
        self._point_to_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        check_ys = self._x_to_y[point[0]]
        all_counts = 0
        for y in check_ys:
            if y == point[1]:  # We won't count "squares" of side length 0
                continue
            delta = y - point[1]
            right_checks = [
                (point[0] + delta, point[1]),
                (point[0] + delta, point[1] + delta),
            ]
            left_checks = [
                (point[0] - delta, point[1]),
                (point[0] - delta, point[1] + delta),
            ]
            right = (
                self._point_to_count[right_checks[0]]
                * self._point_to_count[right_checks[1]]
            )
            left = (
                self._point_to_count[left_checks[0]]
                * self._point_to_count[left_checks[1]]
            )
            all_counts += (right + left) * self._point_to_count[(point[0], y)]
        return all_counts
