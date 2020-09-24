
import unittest


class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_add(self):
        print("1是否等于4")
        self.assertEqual(1, 4)



if __name__ == '__main__':
    unittest.main()