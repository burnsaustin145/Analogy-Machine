import unittest
import networkx as nx
from graph_util import analyze_graph
from complexobject import ComplexObject
from pickle_graph import create_and_pickle_graph
import os

class TestPickleLoad(unittest.TestCase):

    def setUp(self):
        self.curr_object = ComplexObject(pickle_path="wiki_graph.pickle")
        self.graph = self.curr_object.graph
        print(type(self.graph))

    def test_load_graph(self):
        self.assertGreater(self.graph.number_of_nodes(), 0)

    def test_save_graph(self):
        create_and_pickle_graph("Python (programming language)", "wiki_graph.pickle")
        self.assertTrue(os.path.exists("wiki_graph.pickle"))



if __name__ == "__main__":
    unittest.main() 


