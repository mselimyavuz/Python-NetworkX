from erdos_renyi_random_network import ERNetwork, draw_graph

deneme1 = ERNetwork(150, 5000)
deneme = deneme1.ego_network(95)

deneme1.draw_er_graph()
draw_graph(deneme)