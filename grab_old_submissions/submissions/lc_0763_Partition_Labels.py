class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letter_to_start, sorted_starts,start_to_end,result = {},[],{},[]
        for i in range(len(s)):
            letter = s[i]
            if letter_to_start.get(letter) is None:
                sorted_starts.append(i)
                letter_to_start[letter] = i
            start_to_end[letter_to_start[letter]] = i
        if len(sorted_starts) == 1:
            return [len(s)]
        left, right = 0,start_to_end[0]
        for start in sorted_starts[1:]:
            if start < right:
                right = max(start_to_end[start],right) # UGH forgot max here
            else:
                result.append(right-left+1)
                left, right = start, start_to_end[start]
        result.append(right-left+1)
        return result