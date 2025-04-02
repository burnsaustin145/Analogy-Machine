#!/usr/bin/env python
# pickle_graph.py
import pickle
import os
from complexobject import ComplexObject
from wiki_util import WikiUtil

def create_and_pickle_graph(page_title="Python (programming language)", pickle_file="wiki_graph.pickle"):
    """
    Creates a graph by parsing a Wikipedia page and pickles it to a file.
    
    Args:
        page_title: The Wikipedia page title to parse
        pickle_file: The file to save the pickled graph to
    """
    print(f"Creating graph from Wikipedia page: {page_title}")
    wiki = WikiUtil()
    complex_obj = wiki.parse_to_complex_object(page_title)
    
    # Save the ComplexObject to a pickle file
    with open(pickle_file, 'wb') as f:
        pickle.dump(complex_obj, f)
    
    print(f"Graph successfully pickled to {pickle_file}")
    return complex_obj

def load_pickled_graph(pickle_file="wiki_graph.pickle"):
    """
    Loads a pickled graph from a file.
    
    Args:
        pickle_file: The file to load the pickled graph from
        
    Returns:
        The loaded ComplexObject
    """
    if not os.path.exists(pickle_file):
        raise FileNotFoundError(f"Pickle file not found: {pickle_file}")
    
    with open(pickle_file, 'rb') as f:
        complex_obj = pickle.load(f)
    
    print(f"Graph successfully loaded from {pickle_file}")
    return complex_obj

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Create and pickle a Wikipedia knowledge graph")
    parser.add_argument("--create", action="store_true", help="Create and pickle a new graph")
    parser.add_argument("--page", type=str, default="Python (programming language)", 
                        help="Wikipedia page title to parse")
    parser.add_argument("--file", type=str, default="wiki_graph.pickle", 
                        help="Pickle file name")
    
    args = parser.parse_args()
    
    if args.create:
        create_and_pickle_graph(args.page, args.file)
    else:
        try:
            complex_obj = load_pickled_graph(args.file)
            print(f"Loaded graph has {len(complex_obj.graph.nodes())} nodes and {len(complex_obj.graph.edges())} edges")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            print("Run with --create flag to create a new pickled graph") 