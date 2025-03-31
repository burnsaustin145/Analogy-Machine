from complexobject import *
from wiki_util import WikiUtil
import pprint
import networkx as nx

if __name__ == "__main__":
    # Initialize WikiUtil and parse a Wikipedia page
    wiki = WikiUtil()
    page_title = "Python (programming language)"
    print(f"Parsing Wikipedia page: {page_title}")
    complex_obj = wiki.parse_to_complex_object(page_title)

    # Print initial graph structure
    print("\nInitial graph structure from Wikipedia:")
    for node in complex_obj.graph.nodes():
        if len(dict(complex_obj.graph[node])) > 0:  # Only print nodes with edges
            print(f"{node}: {dict(complex_obj.graph[node])}")

    # Test complex constructions with sample nodes
    sample_nodes = ["python", "programming"]
    print(f"\nComplex universe construction test ({', '.join(sample_nodes)}):")
    print(complex_obj.complex_universe_construction(*sample_nodes))

    print(f"\nComplex quality construction test ({', '.join(sample_nodes)}):")
    print(complex_obj.complex_quality_construction(*sample_nodes))

    print(f"\nComplex object construction test ({', '.join(sample_nodes)}):")
    print(complex_obj.complex_object_construction(*sample_nodes))

    # Print final graph structure (limited to nodes with edges)
    print("\nFinal graph structure:")
    for node in complex_obj.graph.nodes():
        if len(dict(complex_obj.graph[node])) > 0:
            print(f"{node}: {dict(complex_obj.graph[node])}")