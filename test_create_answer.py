import unittest

from main import create_answer


class MyTestCase(unittest.TestCase):

    def test_1(self):
        self.assertEqual('Ссылка некорректна. Попробуй другую.', create_answer('https://github.com'))


if __name__ == '__main__':
    unittest.main()
