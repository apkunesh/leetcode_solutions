from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        row = [set() for j in range(n)]
        hits = [row.copy() for i in range(n)]
        output_line = "." * n
        candidate = [output_line for i in range(n)]
        solution = []

        def add_queen(i, j, hits):
            candidate[i] = (
                output_line[i][0:j] + "Q" + output_line[j + 1 :]
                if j < n - 1
                else output_line[i][0:j] + "Q"
            )
            for i_iter in range(i + 1, n):  # Only update rows below
                x_diff = i_iter - i
                l_diag = j - x_diff
                center = j
                r_diag = j + x_diff
                if l_diag > -1:
                    hits[i_iter][l_diag].add(i)
                hits[i_iter][center].add(i)
                if r_diag < n:
                    hits[i_iter][r_diag].add(i)

        def remove_queen(i, j, hits):
            candidate[i] = (
                output_line[i][0:j] + "." + output_line[j + 1 :]
                if j < n - 1
                else output_line[i][0:j] + "."
            )
            for i_iter in range(i + 1, n):
                x_diff = i_iter - i
                l_diag = j - x_diff
                center = j
                r_diag = j + x_diff
                if l_diag > -1:
                    hits[i_iter][l_diag].remove(i)
                hits[i_iter][center].remove(i)
                if r_diag < n:
                    hits[i_iter][r_diag].remove(i)

        # Now we do DFS, attempting to add queens.
        # Base case 1: cannot add, return
        # Final case: can add queen + am at last i; append soln to list; pop queen and return.
        # recursive case: add queen at current position, then attempt to add queen in next row at all js. After this, pop the current queen.
        def recurse(hits, i, j):
            if hits[i][j] != set():
                return
            if i == n - 1:
                add_queen(i, j, hits)
                solution.append(candidate)
                remove_queen(i, j, hits)
            else:
                add_queen(i, j, hits)
                for j in range(n):
                    recurse(hits, i + 1, j)
                remove_queen(i, j, hits)

        for j in range(n):
            recurse(hits, 0, j)
        return solution
