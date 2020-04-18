# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LRUCache:

    class Item:
        def __init__(self, key: int, value: int):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = dict()
        self._head = LRUCache.Item(0, 0)
        self._tail = LRUCache.Item(0, 0)  # Least recent visited node.
        self._head.next = self._tail
        self._tail.prev = self._head

    def _insert_head(self, item: Item) -> None:
        item.next = self._head.next
        self._head.next.prev = item
        item.prev = self._head
        self._head.next = item

    def _remove_tail(self) -> None:
        item = self._tail.prev
        item.prev.next = self._tail
        self._tail.prev = item.prev

    def _detach_item(self, item) -> None:
        item.prev.next = item.next
        item.next.prev = item.prev

    def get(self, key: int) -> int:
        item = self._cache.get(key)
        if item is None:
            return -1
        # Remove item from list.
        self._detach_item(item)
        
        # Move item to head.
        self._insert_head(item)
        return item.value

    def put(self, key: int, value: int) -> None:
        item = self._cache.get(key)
        if item is None:
            if len(self._cache) == self._capacity:
                self._cache.pop(self._tail.prev.key)
                # Remove item from tail.
                self._remove_tail()

            item = LRUCache.Item(key, value)
            self._cache[key] = item
        else:
            item.value = value
            self._detach_item(item)
        self._insert_head(item)