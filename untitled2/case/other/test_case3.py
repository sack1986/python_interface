
import unittest


class TestAdd(unittest.TestCase):
    def setUp(self):
        print("test case start")

    def tearDown(self):
        print("test case end")

    def test_add3(self):
        print("1是否等于3")
        self.assertEqual(1, 3)



if __name__ == '__main__':
    unittest.main()