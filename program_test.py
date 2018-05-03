import unittest

class ATest(unittest.TestCase):
    def setUp(self):
        print("set-up")

    def test_function_x(self):
        print('function test')

    def tearDown(self):
        print("tear-down")


if __name__ == "__main__":
    unittest.main()