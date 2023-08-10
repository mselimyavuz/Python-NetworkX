##
## Implementation of Watts-Strogatz Small World Network Model
## 2023-08-10
## by M. Selim  Yavuz
##

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class WSNetwork(nx.Graph):
    def __init__(self, incoming_graph_data=None, **attr):
        super().__init__(incoming_graph_data, **attr)
        
        self.name = attr.get("name", "Graph")
        self.node_number = attr.get("n", 1)
        self.degree_avg = attr.get("c", 0)
        if self.degree_avg == 1:
            raise ValueError("invalid degree average, needs to be at least 2.")
        
        self.randomness = attr.get("beta", 1)
        
        nodes = [i for i in range(self.node_number)]
        self.add_nodes_from(nodes)

        target_deg = 2
        while target_deg <= self.degree_avg:
            self.add_edges(target_deg)
            target_deg += 1
        print("avg degree: ", sum(dict(self.degree()).values())/len(list(self.nodes)))
        
        to_be_removed = []
        to_be_added = []
        for u, v in self.edges:
            if np.random.uniform(0, 1) < self.randomness:
                to_be_removed.append((u,v))
                random_target = nodes[np.random.randint(0,self.node_number)]
                while random_target == u:
                    random_target = nodes[np.random.randint(0,self.node_number)]
                to_be_added.append((u, random_target))
        for edge in to_be_removed:
            self.remove_edge(edge[0], edge[1])
        for edge in to_be_added:
            self.add_edge(edge[0], edge[1])
        
    def add_edges(self, target_deg):
        nodes = list(self.nodes)
        offset = target_deg - 1
        end = False
        for index, curr_node in enumerate(nodes):
            if index % target_deg != 0 or index-1 % target_deg != 0:
                if self.degree[index] < target_deg and not end:
                    if (index+offset) < len(nodes):
                        self.add_edge(nodes[index], nodes[index+offset])
                    else:
                        end = True
                        if self.degree[0] < target_deg:
                            self.add_edge(nodes[index], nodes[0])
        
    def draw_graph(self):
        nx.draw(self, with_labels=True, node_color='skyblue', font_weight='bold')
        plt.title(self.name)
        plt.show()