import unittest
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title

class TestSearch(unittest.TestCase):
    def test_search_case_insensitive(self):
        dvd = DigitalVideoDisc("The Lion King")
        results = search_by_title([dvd], "lion")
        self.assertEqual(len(results), 1)

if __name__ == '__main__':
    unittest.main()
