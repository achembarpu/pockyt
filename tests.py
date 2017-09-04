import unittest
import collections

from pockyt.client import Client

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self._client = Client(None, None)

    def test_returns_tags_as_sorted_list(self):
        tags = self._client._displayTags(self.newTagDictionary())
        self.assertEqual(tags, ['tag1', 'tag2', 'tag3'])

    def test_returns_empty_list_when_there_are_no_tags(self):
        tags = self._client._displayTags(None)
        self.assertEqual(tags, [])

    def newTagDictionary(self):
        d = {
        "tag1": "object B",
        "tag2": "object A",
        "tag3": "object Z",
        }
        return collections.OrderedDict(sorted(d.items(), key=lambda x:x[1]))

if __name__ == '__main__':
    unittest.main()
