import unittest

from pockyt.client import Client

class TestStringMethods(unittest.TestCase):

    def test_pockyt(self):
        c = Client(None, None)
        tags = c._displayTags('tags')
        self.assertEqual(tags, 'tags')

if __name__ == '__main__':
    unittest.main()
