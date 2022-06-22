import unittest

from l0093_restore_ip_addresses import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          ["255.255.11.135","255.255.111.35"], 
          Solution().restoreIpAddresses('25525511135'))
        self.assertEqual(
          ["0.0.0.0"], 
          Solution().restoreIpAddresses('0000'))
        self.assertEqual(
          ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"], 
          Solution().restoreIpAddresses("101023"))
        