import unittest
from main import search
import os

QUANTITY = int(os.environ['QUANTITY'])

def generate_linear_sequence() :
	for i in range(QUANTITY):
		yield i

class TestStringMethods(unittest.TestCase):

    def test_search_5_some_result(self):
    	self.assertTrue(True)
    	searcher = search(generate_linear_sequence(), lambda vertex: vertex.value >= 5)
    	print([item for item in searcher])

if __name__ == '__main__':
    unittest.main()