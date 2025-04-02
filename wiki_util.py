# wiki_util.py
# Utility to fetch and process Wikipedia content into a ComplexObject
import pickle
import subprocess
import sys
import os

import requests
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from complexobject import ComplexObject
import networkx as nx
import stanza



class WikiUtil:
    def __init__(self, visualize=False):
        """Initialize with an empty ComplexObject using NetworkX"""
        self.graph = nx.DiGraph()
        self.complex_obj = ComplexObject(self.graph)
        stanza.download('en')  # Download English models
        self.parse = stanza.Pipeline('en', device='cuda', processors='tokenize,mwt,pos,lemma,depparse')
        self.visualize = visualize
    def fetch_wikipedia_content(self, title):
        """Fetch raw content from Wikipedia using MediaWiki API"""
        url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "titles": title,
            "prop": "extracts",
            "explaintext": True,
            "format": "json"
        }
        response = requests.get(url, params=params)
        data = response.json()
        
        # Extract page content
        pages = data["query"]["pages"]
        page_id = next(iter(pages))
        if page_id == "-1":
            raise ValueError(f"Page '{title}' not found")
        return pages[page_id]["extract"]

    def parse_to_complex_object(self, title):
        """Parse Wikipedia content into a ComplexObject"""
        import matplotlib.pyplot as plt

        # Fetch content
        content = self.fetch_wikipedia_content(title)
        curr_graph = nx.DiGraph()
        curr_doc = self.parse(content)
        
        # Visualize the first 5 sentences
        for i, sentence in enumerate(curr_doc.sentences):
            # Add nodes for each word in the sentence
            for word in sentence.words:
                curr_graph.add_node(word.text)
            
            # Add edges based on dependency parsing
            for word in sentence.words:
                if word.head != 0:
                    curr_graph.add_edge(word.text, sentence.words[word.head - 1].text, weight=1)
                    print("curr edge: ", word.text, sentence.words[word.head - 1].text)
            
            if i < 5 and self.visualize:
                # Visualize the graph after each sentence
                plt.figure(figsize=(12, 8))
                pos = nx.spring_layout(curr_graph)
                nx.draw(curr_graph, pos, with_labels=True, node_color='lightblue', 
                       node_size=100, font_size=8, font_weight='bold', arrows=True)
                plt.title(f"Sentence {i+1} Dependency Graph")
                plt.savefig(f'sentence_{i+1}_graph.png')
                plt.close()

        self.complex_obj.graph = curr_graph
        return self.complex_obj

    def get_complex_object(self):
        """Return the ComplexObject instance"""
        return self.complex_obj 
    
    def save_complex_object(self, pickle_file="wiki_graph.pickle"):
        """Save the ComplexObject to a pickle file"""
        with open(pickle_file, 'wb') as f:
            pickle.dump(self.complex_obj, f)
        print(f"ComplexObject saved to {pickle_file}")
        
    def load_complex_object(self, pickle_file="wiki_graph.pickle"):
        """Load a ComplexObject from a pickle file"""
        if not os.path.exists(pickle_file):
            raise FileNotFoundError(f"Pickle file not found: {pickle_file}")
        
        with open(pickle_file, 'rb') as f:
            self.complex_obj = pickle.load(f)
        
        print(f"ComplexObject loaded from {pickle_file}")
        return self.complex_obj


