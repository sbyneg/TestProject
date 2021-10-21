-- * code:utf-8 * --
import unittest

class MyTestCase(unittest.TestCase):
    def test_something(self,mes):
        self.assertEqual(100, “结果错误”)

if __name__ == '__main__':
    unittest.main()
    ...
