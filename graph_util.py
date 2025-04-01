# graph_util.py
# Utility functions for analyzing graph characteristics from ComplexObject

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from complexobject import ComplexObject

def analyze_graph(graph):
    """
    Analyze various characteristics of a graph and return a dictionary of metrics.
    
    Args:
        graph: A NetworkX graph object
        
    Returns:
        dict: Dictionary containing various graph metrics
    """
    metrics = {}
    
    # Basic graph information
    metrics['num_nodes'] = graph.number_of_nodes()
    metrics['num_edges'] = graph.number_of_edges()
    
    if metrics['num_nodes'] > 0:
        # Connectivity metrics
        if nx.is_connected(graph.to_undirected()):
            metrics['is_connected'] = True
            metrics['avg_shortest_path'] = nx.average_shortest_path_length(graph.to_undirected())
        else:
            metrics['is_connected'] = False
            metrics['connected_components'] = nx.number_connected_components(graph.to_undirected())
        
        # Degree metrics
        degrees = [d for n, d in graph.degree()]
        metrics['avg_degree'] = np.mean(degrees)
        metrics['max_degree'] = max(degrees)
        metrics['min_degree'] = min(degrees)
        
        # Centrality metrics
        metrics['degree_centrality'] = nx.degree_centrality(graph)
        metrics['betweenness_centrality'] = nx.betweenness_centrality(graph)
        metrics['closeness_centrality'] = nx.closeness_centrality(graph)
        
        # Clustering and density
        metrics['density'] = nx.density(graph)
        metrics['avg_clustering'] = nx.average_clustering(graph.to_undirected())
        
        # Try to calculate diameter (only works for connected graphs)
        try:
            metrics['diameter'] = nx.diameter(graph.to_undirected())
        except nx.NetworkXError:
            metrics['diameter'] = 'Graph is not connected'
    
    return metrics

def visualize_graph(graph, title="Graph Visualization", save_path=None):
    """
    Visualize a graph with node sizes based on degree centrality.
    
    Args:
        graph: A NetworkX graph object
        title: Title for the visualization
        save_path: Path to save the visualization (if None, display instead)
    """
    plt.figure(figsize=(12, 10))
    
    # Calculate node sizes based on degree centrality
    centrality = nx.degree_centrality(graph)
    node_sizes = [centrality[n] * 5000 + 100 for n in graph.nodes()]
    
    # Use spring layout for node positioning
    pos = nx.spring_layout(graph, seed=42)
    
    # Draw the graph
    nx.draw_networkx(
        graph,
        pos=pos,
        with_labels=True,
        node_color='lightblue',
        node_size=node_sizes,
        font_size=8,
        font_weight='bold',
        edge_color='gray',
        width=0.5,
        alpha=0.8
    )
    
    plt.title(title)
    plt.axis('off')
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.close()
    else:
        plt.show()

def compare_graphs(graph1, graph2, metrics_to_compare=None):
    """
    Compare two graphs based on selected metrics.
    
    Args:
        graph1: First NetworkX graph
        graph2: Second NetworkX graph
        metrics_to_compare: List of metrics to compare (if None, compare all common metrics)
        
    Returns:
        dict: Dictionary with comparison results
    """
    metrics1 = analyze_graph(graph1)
    metrics2 = analyze_graph(graph2)
    
    comparison = {}
    
    if metrics_to_compare is None:
        # Compare all scalar metrics
        scalar_metrics = [
            'num_nodes', 'num_edges', 'avg_degree', 'max_degree', 'min_degree',
            'density', 'avg_clustering'
        ]
        
        if metrics1.get('is_connected', False) and metrics2.get('is_connected', False):
            scalar_metrics.append('avg_shortest_path')
            scalar_metrics.append('diameter')
            
        metrics_to_compare = scalar_metrics
    
    for metric in metrics_to_compare:
        if metric in metrics1 and metric in metrics2:
            if isinstance(metrics1[metric], (int, float)) and isinstance(metrics2[metric], (int, float)):
                comparison[metric] = {
                    'graph1': metrics1[metric],
                    'graph2': metrics2[metric],
                    'difference': metrics2[metric] - metrics1[metric],
                    'percent_change': ((metrics2[metric] - metrics1[metric]) / metrics1[metric] * 100) 
                                     if metrics1[metric] != 0 else float('inf')
                }
    
    return comparison

if __name__ == "__main__":
    # Example usage
    from wiki_util import WikiUtil
    
    # Initialize WikiUtil and parse a Wikipedia page
    wiki = WikiUtil()
    page_title = "Python (programming language)"
    print(f"Analyzing Wikipedia page: {page_title}")
    complex_obj = wiki.parse_to_complex_object(page_title)
    
    # Analyze the graph
    metrics = analyze_graph(complex_obj.graph)
    
    # Print metrics
    print("\nGraph Metrics:")
    for key, value in metrics.items():
        if not isinstance(value, dict):
            print(f"{key}: {value}")
    
    # Visualize the graph
    visualize_graph(complex_obj.graph, title=f"Graph for '{page_title}'", save_path="wiki_graph.png")
    
    print("\nGraph visualization saved to 'wiki_graph.png'")
