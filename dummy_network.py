import networkx as nx
import matplotlib.pyplot as plt

# create a graph
G = nx.karate_club_graph()

# calculate betweenness centrality
betweenness = nx.betweenness_centrality(G)

# scale betweenness centrality to node sizes
scaling_factor = 500
node_sizes = [betweenness[node] * scaling_factor for node in G.nodes()]

# draw the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color="lightblue")
nx.draw_networkx_edges(G, pos, edge_color="gray")
nx.draw_networkx_labels(G, pos, font_size=10, font_family="Arial")
plt.axis("off")
plt.show()

print("Number of nodes: ", nx.number_of_nodes(G))
print("Number of edges: ", nx.number_of_edges(G))
print("Density: ", nx.density(G))
print("Average shortest path length: ", nx.average_shortest_path_length(G))
print("Average clustering coefficient: ", nx.average_clustering(G))
print("Degree histogram: ", nx.degree_histogram(G))

# Get the degree distribution
degrees = [G.degree(n) for n in G.nodes()]
degree_hist = nx.degree_histogram(G)

# Plot the degree histogram
plt.hist(degrees, bins=len(degree_hist), align='left', rwidth=0.8)
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Histogram')
plt.show()