#-*- coding:utf-8 -*- 
import unittest
from src.maximum_sum import prepar_vector, execute_sum, print_interval

class TestMaximumSum(unittest.TestCase):
    def setUp(self):
        self.vector = [2, -4, 6, 8, -10, 100, -6, 5]

    def test_prepar_vector(self):
        self.assertEquals(self.vector , prepar_vector("2,-4,6,8,-10,100,-6,5"))

    def test_execute_sum(self):
        self.assertEquals([6, 8, -10, 100], execute_sum(self.vector))

    def test_print_interval(self):
        sub_vector = [6, 8, -10, 100]
        self.assertEquals((2, 5), print_interval(sub_vector,self.vector))
    
if __name__ == "__main__":
    unittest.main()