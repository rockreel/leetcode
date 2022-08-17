from collections import deque, Counter, defaultdict
from typing import List
import time
from collections import deque

class RateLimiterAllRequests:
    
    def __init__(self, qps):
        self._qps = qps
        self._requests = deque()
        
    def should_accept_request(self):
        print(self._requests)
        timestamp = time.time()
        time_boundary = time.time() - 1.0
        while self._requests and self._requests[0] < time_boundary:
            self._requests.popleft()
            
        if len(self._requests) < self._qps:
            self._requests.append(timestamp)
            return True
        else:
            return False
        
class RateLimiterSimpleCounter:
    
    def __init__(self, qps):
        self._qps = qps
        self._counter = [int(time.time()), 0]
        
    def should_accept_request(self):
        timestamp = int(time.time())
        if timestamp == self._counter[0]:
            if self._counter[1] < self._qps:
                self._counter[1] += 1
                return True
            else:
                return False
        else:
            self._counter = [timestamp, 1]
            return True
    

class RateLimiterSlidingWindow:

    def __init__(self, qps):
        self._qps = qps
        self._counter = [int(time.time()), 0]
        self._counter_prev = 0
        
    def should_accept_request(self):
        timestamp = time.time()
        # Rotate counter.
        if int(timestamp) != self._counter[0]:
            self._counter_prev = self._counter[1]
            self._counter = [int(timestamp), 0]
        
        curr_qps = (1.0 - (timestamp - int(timestamp)) / 1.0) * self._counter_prev + self._counter[1]
        if int(curr_qps) < self._qps:
            self._counter[1] += 1
            return True
        else:
            return False
                
r = RateLimiterSlidingWindow(5)        
print(r.should_accept_request())
print(r.should_accept_request())
print(r.should_accept_request())
print(r.should_accept_request())
print(r.should_accept_request())
print(r.should_accept_request())
print(r.should_accept_request())
print(r.should_accept_request())
time.sleep(1)
print(r.should_accept_request())
print(r.should_accept_request())
print(r.should_accept_request())
print(r.should_accept_request())