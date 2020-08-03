import unittest

from Pythonbasics.week_1 import Spiral


class MyTestCase(unittest.TestCase):
    def test_something(self):
        spiral=Spiral(4).main()
        array=spiral.arr[0][2]
        self.assertEqual(3,array)


if __name__ == '__main__':
    unittest.main()
