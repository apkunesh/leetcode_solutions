from collections import defaultdict


class Solution:
    def countHomogenous(self, s: str) -> int:
        if len(s) == 1:
            return 1  # just in case
        contig_to_count = defaultdict(int)
        counts = set()
        n_letters, cur_letter = 1, s[0]
        for i in range(1, len(s)):
            if s[i] == cur_letter:
                n_letters += 1
            else:
                counts.add(n_letters)
                contig_to_count[n_letters] += 1
                n_letters, cur_letter = 1, s[i]
        counts.add(n_letters)
        counts = list(counts)
        counts.sort()
        contig_to_count[n_letters] += 1
        local_result, grand_result = 0, 0
        for i in range(counts[-1] + 1):
            local_result += i
            grand_result += local_result * contig_to_count[i]
        return grand_result % (10**9 + 7)
