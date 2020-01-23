
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import networkx as nx

import requests

response = requests.get('http://localhost:3000/')
resData = response.json()

G = nx.Graph()

G.add_edge(str(resData[0]['importedFile']), str(resData[3]['importedFile']), weight=0.7)
G.add_edge(str(resData[3]['importedFile']), str(resData[2]['importedFile']), weight=0.5)

G.add_edge(str(resData[2]['importedFile']), str(resData[4]['importedFile']), weight=0.5)
G.add_edge(str(resData[4]['importedFile']), str(resData[1]['importedFile']), weight=0.7)


#

elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] > 0.5]
esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d['weight'] <= 0.5]

pos = nx.spring_layout(G)  # positions for all nodes

# nodes
nx.draw_networkx_nodes(G, pos, node_size=600)

# edges
nx.draw_networkx_edges(G, pos, edgelist=elarge,
                       width=6)
nx.draw_networkx_edges(G, pos, edgelist=esmall,
                       width=6, alpha=0.5, edge_color='b')

# labels
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

plt.axis('off')
plt.show()
