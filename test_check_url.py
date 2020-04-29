import unittest

from main import check_url


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertTrue(check_url('https://github.com/git'))

    def test_2(self):
        self.assertFalse(check_url('https://github.com'))

    def test_3(self):
        self.assertFalse(check_url('https://github.com/'))

    def test_4(self):
        self.assertTrue(check_url('https://github.com/a'))

    def test_5(self):
        self.assertTrue(check_url('  https://github.com/a  '))


if __name__ == '__main__':
    unittest.main()
