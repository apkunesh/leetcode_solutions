class LRUCache:
    # Really horrid problem, needed queues and two maps.
    # Basic idea:
    # Create a queue for each "use" of keys, pushes and gets
    # Create a map for # uses of each key
    # When pushing or getting, push to the queue and increment
    # the value of the use map for the key
    # When capacity is exceeded, pop from the queue
    # and decrement the corresponding use map value
    # until a queue element drops a use map value to 0.
    # This key is least-recently used and can be `popped`
    # from teh main cache.
    def __init__(self, capacity: int):
        self.queue = deque() # append, popleft
        self.call_map = {}
        self.cache = {}
        self.max_size = capacity


    def get(self, key: int) -> int:
        potential_result = self.cache.get(key)
        if potential_result is not None:
            self.queue.append(key)
            self.call_map[key] += 1
            return potential_result
        return -1

    def put(self, key: int, value: int) -> None:
        self.queue.append(key)
        if self.call_map.get(key) == None:
            self.call_map[key] = 1
        else:
            self.call_map[key] += 1
        self.cache[key] = value

        if len(self.cache) > self.max_size:
            key_deleted = False
            while key_deleted == False:
                oldest_key = self.queue.popleft()
                self.call_map[oldest_key] -= 1
                if self.call_map[oldest_key] == 0:
                    self.cache.pop(oldest_key)
                    self.call_map.pop(oldest_key)
                    key_deleted = True