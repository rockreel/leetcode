class MyHashMap:

    def __init__(self):
        self.size = 100
        self.buckets = [[] for _ in range(self.size)]

    def hash(self, key: int) -> int:
        return key % self.size

    def put(self, key: int, value: int) -> None:
        bucket = self.buckets[self.hash(key)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key: int) -> int:
        bucket = self.buckets[self.hash(key)]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        bucket = self.buckets[self.hash(key)]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)