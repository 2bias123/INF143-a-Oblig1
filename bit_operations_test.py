import unittest
import bit_operations as bit_op


class TestStringMethods(unittest.TestCase):

    def  setUp(self) -> None:
        self.testcase1 = [1,0,1,0,1]
        self.testcase2 = [1,1,1,0,0]
    
    def test_lst_xor(self):
        self.assertListEqual(bit_op.lstxor(self.testcase1,self.testcase2),[0,1,0,0,1])

    def test_bitwise_and_lst(self):
        self.assertListEqual(bit_op.bitwise_and_lst(self.testcase1,self.testcase2),[1,0,1,0,0])

    def test_left_cyclic_shift(self):
        with self.subTest():
            self.assertListEqual(bit_op.left_cyclic_shift(self.testcase1,1),[0,1,0,1,1])
        with self.subTest():
            self.assertListEqual(bit_op.left_cyclic_shift(self.testcase1,2),[1,0,1,1,0])

    def test_right_cyclic_shift(self):
        with self.subTest():
            self.assertListEqual(bit_op.right_cyclic_shift(self.testcase1,1),[1,1,0,1,0])
        with self.subTest():
            self.assertListEqual(bit_op.right_cyclic_shift(self.testcase1,2),[0,1,1,0,1])
    
if __name__ == '__main__':
    unittest.main()