import unittest

from l0164_maximum_gap import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().maximumGap([3, 6, 9, 1]))
        self.assertEqual(0, Solution().maximumGap([10]))
        self.assertEqual(0, Solution().maximumGap([1, 1, 1, 1]))
        self.assertEqual(9999999, Solution().maximumGap([1, 10000000]))
        self.assertEqual(
            1244,
            Solution().maximumGap([
                12115,10639,2351,29639,31300,11245,16323,24899,8043,4076,17583,
                15872,19443,12887,5286,6836,31052,25648,17584,24599,13787,24727,
                12414,5098,26096,23020,25338,28472,4345,25144,27939,10716,3830,
                13001,7960,8003,10797,5917,22386,12403,2335,32514,23767,1868,
                29882,31738,30157,7950,20176,11748,13003,13852,19656,25305,7830,
                3328,19092,28245,18635,5806,18915,31639,24247,32269,29079,24394,
                18031,9395,8569,11364,28701,32496,28203,4175,20889,28943,6495,
                14919,16441,4568,23111,20995,7401,30298,2636,16791,1662,27367,
                2563,22169,1607,15711,29277,32386,27365,31922,26142,8792
            ]))
        