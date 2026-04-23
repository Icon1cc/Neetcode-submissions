class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def _hash(self, key: int) -> int:
        return key % self.size
        

    def put(self, key: int, value: int) -> None:
        id = self._hash(key)

        for pair in self.buckets[id]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[id].append([key, value])

    def get(self, key: int) -> int:
        id = self._hash(key)

        for pair in self.buckets[id]:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        id = self._hash(key)

        for pair in self.buckets[id]:
            if pair[0] == key:
                self.buckets[id].remove(pair)

                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)