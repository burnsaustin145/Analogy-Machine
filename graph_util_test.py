import unittest
from graph_util import test_graph_characteristics, print_graph_characteristics
from wiki_util import WikiUtil

class TestGraphUtil(unittest.TestCase):
    def setUp(self):
        self.wiki = WikiUtil()

    def test_graph_characteristics(self):
        page_title = "Python (programming language)"
        complex_obj = self.wiki.parse_to_complex_object(page_title)
        results = test_graph_characteristics(complex_obj)
        assert results['average_connectivity'] > 0
        assert results['number_of_nodes'] > 0
        assert results['number_of_edges'] > 0
        assert results['density'] > 0
        assert results['average_clustering'] > 0
        print_graph_characteristics(complex_obj)

if __name__ == "__main__":
    unittest.main()

