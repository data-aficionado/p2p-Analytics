import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import networkx as nx

def visualize_heatmap(input_file):
    # Load differential expression data
    data = pd.read_csv(input_file)
    
    # Create heatmap
    sns.heatmap(data.pivot("gene", "condition", "expression"), cmap="viridis")
    plt.show()

def visualize_network(input_file):
    # Load co-expression network
    G = nx.read_gml(input_file)
    
    # Create network plot
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color="skyblue", edge_color="gray", node_size=20, font_size=10)
    plt.show()

if __name__ == "__main__":
    visualize_heatmap("differential_expression_results.csv")
    visualize_network("co_expression_network.gml")
