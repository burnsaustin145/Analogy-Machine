from complexobject import *
from wiki_util import WikiUtil
import pprint
import networkx as nx
import os
import pickle
from pickle_graph import load_pickled_graph, create_and_pickle_graph

if __name__ == "__main__":
    pickle_file = "wiki_graph.pickle"
    page_title = "Python (programming language)"
    
    # Check if pickled graph exists, create it if it doesn't
    if not os.path.exists(pickle_file):
        print(f"Pickle file not found. Creating new graph from {page_title}...")
        complex_obj = create_and_pickle_graph(page_title, pickle_file)
    else:
        # Load the pickled graph
        print(f"Loading graph from {pickle_file}...")
        complex_obj = load_pickled_graph(pickle_file)

    # Print initial graph structure
    print("\nGraph structure from pickled data:")
    node_count = 0
    for node in complex_obj.graph.nodes():
        if len(dict(complex_obj.graph[node])) > 0:  # Only print nodes with edges
            print(f"{node}: {dict(complex_obj.graph[node])}")
            node_count += 1
            if node_count >= 10:  # Limit output to first 10 nodes
                print("... (more nodes with edges)")
                break

    # Test complex constructions with sample nodes
    sample_nodes = ["python", "programming", "Solaris"]
    print(f"\nComplex universe construction test ({', '.join(sample_nodes)}):")
    print(complex_obj.complex_universe_construction(*sample_nodes))

    print(f"\nComplex quality construction test ({', '.join(sample_nodes)}):")
    print(complex_obj.complex_quality_construction(*sample_nodes))

    print(f"\nComplex object construction test ({', '.join(sample_nodes)}):")
    print(complex_obj.complex_object_construction(*sample_nodes))

    # Print final graph structure (limited to nodes with edges)
    print("\nFinal graph structure (after operations):")
    
    # Visualize the graph using networkx and matplotlib
    import matplotlib.pyplot as plt
    print("Visualizing the graph...")
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(complex_obj.graph)
    nx.draw(complex_obj.graph, pos, with_labels=True, node_color='lightblue', 
           node_size=100, font_size=8, font_weight='bold')
    plt.title("Wikipedia Knowledge Graph")
    plt.savefig('wiki_graph.png')
    plt.close()
   