from random import randint


class RandomizedSet:
    # TODO: Each must average to 0(1)
    def __init__(self):
        self._index_to_val = {}
        self._val_to_index = {}
        self._index = 0

    def insert(self, val: int) -> bool:
        if val in self._val_to_index:
            return False
        self._index_to_val[self._index] = val
        self._val_to_index[val] = self._index
        self._index += 1
        # print("State on add val ", val)
        # print(self._val_to_index)
        # print(self._index_to_val)
        return True

    def remove(self, val: int) -> bool:
        # TODO: Removes value from set. Returns value if present, false otherwise.
        if val in self._val_to_index:
            index = self._val_to_index.pop(val)
            # print("popped ", index)
            self._index_to_val.pop(index)
            # print("State on removing val ", val)
            # print(self._val_to_index)
            # print(self._index_to_val)
            return True
        return False

    def getRandom(self) -> int:
        # TODO: Returns random (evenly-weighted) value from set. We're guaranteed to have at least 1 value present.
        # Idea: try to pull value at random index. If value isn't present (Odds are m/n, where n is the # of times remove has been called and n is the number of times insert has been called), reindex (O(n-m)) and retry.
        # Intuition: reindexing is roughly O(N) but should happen with ~1/N probability. Thus should amortize to O(1).
        index = randint(0, self._index - 1)
        if index in self._index_to_val:
            return self._index_to_val[index]
        new_ind_to_val, new_val_to_ind, new_ind = {}, {}, 0
        for item in self._index_to_val.values():
            new_ind_to_val[new_ind] = item
            new_val_to_ind[item] = new_ind
            new_ind += 1
        self._index = new_ind
        self._index_to_val = new_ind_to_val
        self._val_to_index = new_val_to_ind
        index = randint(0, self._index - 1)
        return self._index_to_val[index]  # Note that this is now guaranteed inside.
