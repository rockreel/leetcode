class LRUCache(object):
    class CacheObj(object):
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._capacity = capacity
        self._hash = {}  # key -> CacheObj.
        self._head = self.CacheObj(None, None) # Most recent.
        self._tail = self.CacheObj(None, None) # Least recent.
        self._head.next = self._tail
        self._tail.prev = self._head
        

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self._hash:
            return -1  
        cache_obj = self._hash[key]
        
        # Remove from middle.
        cache_obj.prev.next = cache_obj.next
        cache_obj.next.prev = cache_obj.prev
        
        # Put at the head.
        head = self._head.next
        cache_obj.next = head
        head.prev = cache_obj
        self._head.next = cache_obj
        cache_obj.prev = self._head
            
        return cache_obj.value

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        # Remove one key if reach capacity.
        if key not in self._hash and len(self._hash) == self._capacity: 
            tail = self._tail.prev
            del self._hash[tail.key]
            tail.prev.next = self._tail
            self._tail.prev = tail.prev
            
        # Set key.
        if key in self._hash:
            cache_obj = self._hash[key]
            cache_obj.value = value
            # Access it will make it most recent.
            self.get(key)
        else:
            cache_obj = self.CacheObj(key, value)
            self._hash[key] = cache_obj
            # Insert at head.
            cache_obj.next = self._head.next
            self._head.next.prev = cache_obj
            self._head.next = cache_obj
            cache_obj.prev = self._head

