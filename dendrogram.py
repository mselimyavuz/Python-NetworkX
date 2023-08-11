import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from scipy.cluster.hierarchy import linkage, dendrogram
from watts_strogatz_small_world_network import WSNetwork

num_nodes = 100
G = WSNetwork(n=num_nodes, c=7, beta=0.7)

# Calculate hierarchical clustering
adjacency_matrix = nx.to_numpy_matrix(G)
linkage_matrix = linkage(adjacency_matrix, method='average')

# Create a dendrogram
plt.figure(figsize=(10, 6))
dendrogram(linkage_matrix, labels=[f'Node {i}' for i in range(1, num_nodes + 1)])
plt.xlabel('Nodes')
plt.ylabel('Distance')
plt.title('Dendrogram of Network Data')
plt.show()
