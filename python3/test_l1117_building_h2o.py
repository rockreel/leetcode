import unittest
import threading

from l1117_building_h2o import H2O

class Test(unittest.TestCase):
    
    def test_solution(self):
        h2o = H2O()
        n = 5
        o_threads = []
        h_threads = []

        for _ in range(n):
            t = threading.Thread(target=lambda: h2o.oxygen(lambda: print('O')))
            o_threads.append(t)
            t.start()

        for _ in range(2*n):
            t = threading.Thread(target=lambda: h2o.hydrogen(lambda: print('H')))
            h_threads.append(t)
            t.start()

        [t.join() for t in o_threads]
        [t.join() for t in h_threads]
