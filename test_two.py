from complexobject import *
from wiki_util import WikiUtil
import pprint
import networkx as nx

"""testing the reading in of the graph"""

if __name__ == "__main__":
    # Initialize WikiUtil and parse a Wikipedia page
    import os
    page_title = "Python (programming language"
    pickle_path = "graph.pkl"
    if os.path.exists(pickle_path):
        print(f"Loading graph from '{pickle_path}'")
        complex_obj = ComplexObject(pickle_path=pickle_path)
    else:
        wiki = WikiUtil()
        print(f"Parsing Wikipedia page: {page_title}")
        complex_obj = wiki.parse_to_complex_object(page_title, pickle_path=pickle_path)

    # Print initial graph structure
    """
    print("\nInitial graph structure from Wikipedia:")
    print(nx.write_network_text(complex_obj.graph))
    """
    print(complex_obj.graph.nodes())


