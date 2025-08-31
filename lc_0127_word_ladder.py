from collections import defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 0
        if endWord not in wordList:  # O(n)
            return 0
        # Real algorithm
        seen = set()
        dashed_to_index = defaultdict(set)

        def construct_dashed_words(word_in):
            for i in range(len(word_in)):
                yield (
                    word_in[0:i] + "-" + word_in[i + 1 :]
                    if i < len(word_in) - 1
                    else word_in[0:i] + "-"
                )

        for word_index in range(len(wordList)):
            word = wordList[word_index]
            for dashed_word in construct_dashed_words(word):
                dashed_to_index[dashed_word].add(word_index)
        # Initial Conditions
        tentative_dist = 2
        trial_words = set()
        for word in construct_dashed_words(beginWord):
            for mapped_index in dashed_to_index[word]:
                trial_words.add(wordList[mapped_index])
                seen.add(mapped_index)
        # DFS
        while trial_words:
            # Search for word; if present, return dist to word
            # Be careful not to add words whose index we've already seen.
            next_layer_trial = set()
            for word in trial_words:
                if word == endWord:
                    return tentative_dist
                for dashed_word in construct_dashed_words(word):
                    for mapped_index in dashed_to_index[dashed_word]:
                        if mapped_index in seen:
                            continue
                        next_layer_trial.add(wordList[mapped_index])
                        seen.add(mapped_index)
            trial_words = next_layer_trial
            tentative_dist += 1
        return 0


first_result = Solution().ladderLength(
    "cat", "sag", ["bat", "bag", "sag", "dag", "dot"]
)
second_result = Solution().ladderLength(
    "cat", "sag", ["bat", "bag", "sat", "dag", "dot"]
)
assert first_result == 4, first_result
assert second_result == 0, second_result
