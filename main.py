import networkx as nx

G = nx.Graph()  # Crea un grafo no dirigido

G.add_nodes_from([1,2,3,4,5])
G.add_edges_from([(1,2),(2,3),(3,4),(4,5),(5,1)])


G.add_node("a")
G.add_node("z")

G.add_edge("a", 1)
G.add_edge("z", 5)


import matplotlib.pyplot as plt

nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()

