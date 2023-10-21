import networkx as nx

G = nx.Graph()  # Crea un grafo no dirigido

G.add_node("brandon")
G.add_node("adriana")
G.add_node("joel")
G.add_node("delia")
G.add_node("andrea")
G.add_node("clarissa")
G.add_node("michel")
G.add_node("tadeo")
G.add_node("mariana")
G.add_node("salma")
G.add_node("angel")
G.add_node("luis")
G.add_node("brayan")


brandon_conectados = ["adriana","clarissa","joel","delia","brayan","luis"]
for nodo_conectado in brandon_conectados:
    G.add_edge("brandon", nodo_conectado)
adri_conectados = ["brandon","michel","joel","delia","andrea","tadeo"]
for nodo_conectado in adri_conectados:
    G.add_edge("adriana", nodo_conectado)
clarissa_conectados = ["adriana","brandon","joel","delia","andrea"]
for nodo_conectado in clarissa_conectados:
    G.add_edge("clarissa", nodo_conectado)
delia_conectados = ["adriana","clarissa","joel","andrea","brandon"]
for nodo_conectado in delia_conectados:
    G.add_edge("delia", nodo_conectado)
joel_conectados = ["adriana","clarissa","andrea","delia"]
for nodo_conectado in joel_conectados:
    G.add_edge("joel", nodo_conectado)
michel_conectados = ["adriana","clarissa","delia","tadeo","mariana","luis"]
for nodo_conectado in michel_conectados:
    G.add_edge("michel", nodo_conectado)
angel_conectados = ["luis","brandon","brayan","salma"]
for nodo_conectado in angel_conectados:
    G.add_edge("angel", nodo_conectado)
salma_conectados = ["angel","mariana","tadeo"]
for nodo_conectado in salma_conectados:
    G.add_edge("salma", nodo_conectado)
brayan_conectados = ["angel","brandon","luis","adriana","michel"]
for nodo_conectado in brayan_conectados:
    G.add_edge("brayan", nodo_conectado)





import matplotlib.pyplot as plt

nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
plt.show()

