# wiki_util.py
# Utility to fetch and process Wikipedia content into a ComplexObject
import pickle
import subprocess
import sys

import requests
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from complexobject import ComplexObject
import networkx as nx
import stanza



class WikiUtil:
    def __init__(self):
        """Initialize with an empty ComplexObject using NetworkX"""
        self.graph = nx.DiGraph()
        self.complex_obj = ComplexObject(self.graph)
        stanza.download('en')  # Download English models
        self.parse = stanza.Pipeline('en')

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

        # Fetch content
        content = self.fetch_wikipedia_content(title)
        curr_graph = nx.DiGraph()
        curr_doc = self.parse(content)
        for sentence in curr_doc.sentences:
            for word in sentence.words:
                curr_graph.add_node(word.text)
            
            for word in sentence.words:
                if word.head != 0:
                    curr_graph.add_edge(word.head, word.text, weight=1)
        # Update ComplexObject with the new graph
        print("curr graph: ", curr_graph.nodes())
        self.complex_obj.graph = curr_graph
        return self.complex_obj

    def get_complex_object(self):
        """Return the ComplexObject instance"""
        return self.complex_obj 
    

