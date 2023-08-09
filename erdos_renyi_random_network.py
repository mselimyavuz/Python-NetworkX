##
## Implementation of Erdös-Rényi Random Network Model
## 2023-08-09
## by M. Selim  Yavuz
##

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


class ERNetwork():
    def __init__(self, n=1, m=0, name="Graph") -> None:
        self._node_number = n
        self._edge_number = m
        self._network_name = name
        
        if self._edge_number > ((self._node_number * (self._node_number-1))/2):
            raise ValueError("Edge number is bigger than the maximum value.")
        
        self._er_graph = nx.Graph()
    
        node_list = [i for i in range(self._node_number)]
        self._er_graph.add_nodes_from(node_list)
        
        for e in range(self._edge_number):
            node_1 = np.random.randint(0, self._node_number)
            node_2 = np.random.randint(0, self._node_number)
            
            if not (self._er_graph.has_edge(node_1, node_2) or self._er_graph.has_edge(node_2, node_1)):
                self._er_graph.add_edge(node_1, node_2)
            
    def ego_network(self, ego):
        return nx.ego_graph(self._er_graph, ego, radius=1)

    def add_edge(self, node_1, node_2):
        if not (self._er_graph.has_edge(node_1, node_2) or self._er_graph.has_edge(node_2, node_1)):
                self._er_graph.add_edge(node_1, node_2)
        else:
            print(f"edge {node_1}-{node_2} already exists.")
            
    def draw_er_graph(self):
        nx.draw(self._er_graph, with_labels=True, node_color='skyblue', font_weight='bold')
        plt.title(self._network_name)
        plt.show()


def draw_graph(network, name="Graph"):
    nx.draw(network, with_labels=True, node_color='skyblue', font_weight='bold')
    plt.title(name)
    plt.show()