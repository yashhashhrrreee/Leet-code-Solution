from collections import defaultdict, OrderedDict
class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key -> (freq, val)
        self.frequencies = defaultdict(OrderedDict)
        self.minf = 0
        self.capacity = capacity

    def insert(self, key, frequency, value):
        self.cache[key] = (frequency, value)
        self.frequencies[frequency][key] = value
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        frequency, value = self.cache[key] # a -> 2, 1 ==> 2: []
        del self.frequencies[frequency][key]
        if self.minf == frequency and not self.frequencies[frequency]:
            self.minf += 1
        self.insert(key, frequency+1, value)
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if key in self.cache:
            self.get(key)
            self.cache[key] = (self.cache[key][0], value)
            return
        if self.capacity == len(self.cache):
            k, v = self.frequencies[self.minf].popitem(last=False)
            del self.cache[k]
        self.minf = 1
        self.insert(key, 1, value)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)