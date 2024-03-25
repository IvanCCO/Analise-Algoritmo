import networkx as nx
import matplotlib.pyplot as plt

# Criar um grafo direcionado
G = nx.Graph()

# Adicionar as arestas
edges = [
    ("a", "c"),
    ("a", "f"),
    ("b", "c"),
    ("b", "f"),
    ("c", "d"),
    ("c", "e"),
    ("d", "f"),
    ("e", "f"),
]
G.add_edges_from(edges)

# Desenhar o grafo
nx.draw(
    G,
    with_labels=True,
    node_size=1000,
    node_color="lightgreen",
    font_size=20,
    font_color="black",
    font_weight="bold",
)

# Mostrar o gráfico
plt.show()
