class MyHashSet:

    def __init__(self):
        self.size = 100
        self.buckets = [[] for _ in range(self.size)]
    
    def hash(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        if not self.contains(key):
            self.buckets[self.hash(key)].append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            bucket = self.buckets[self.hash(key)]
            bucket.remove(key)
        
    def contains(self, key: int) -> bool:
        bucket = self.buckets[self.hash(key)]
        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)