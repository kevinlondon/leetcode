from collections import OrderedDict

class LRUCache(object):
    def __init__(self, capacity):
        self.array = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.array:
            value = self.array[key]
            # Remove first
            del self.array[key]
            # Add back in
            self.array[key] = value
            return value
        else:
            return -1

    def put(self, key, value):
        if key in self.array:
            # Delete existing key before refreshing it
            del self.array[key]
        elif len(self.array) >= self.capacity:
            # Delete oldest
            k, v = next(iter(self.array.items()))
            del self.array[k]
        self.array[key] = value


from queue import Queue

class LRUCacheDifferent:

    def __init__(self, capacity: int):
        self.events = Queue()
        self.counts = defaultdict(int)
        self.capacity = capacity
        self.data = {}

    def get(self, key: int) -> int:
        if key in self.data:
            self.events.put(key)
            self.counts[key] += 1
            return self.data[key]

        return -1

    def put(self, key: int, value: int) -> None:
        self.data[key] = value
        self.events.put(key)
        self.counts[key] += 1
        self.clean()

    def clean(self):
        while len(self.data) > self.capacity:
            key = self.events.get()
            self.counts[key] -= 1
            if self.counts[key] <= 0:
                del self.data[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
