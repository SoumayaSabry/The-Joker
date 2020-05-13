#Part1
## to install the library i,t is ( python - m pip -U networkx)
import matplotlib.pyplot as plt
import networkx as nx ## for display 
from Graph import Graph

##Our Graph
graphMap = Graph()
graphMap.InsertGraph_FromCSV("map.csv")
graphMap.initialisationNodes()

#displaying Graph
print("-----------------------------Graph Matrix------------------------------")
graphMap.Graph_ToMatrix()

G = nx.Graph()
for key , val in graphMap.distances.items()  :
	r = list(key)
	G.add_edge(r[0], r[1], weight=val)

# positions for all nodes
pos = nx.spring_layout(G)  
# nodes
nx.draw_networkx_nodes(G, pos, node_size=100)
# edges
nx.draw_networkx_edges(G, pos,width=3)
# labels
nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')
plt.axis('off')
plt.show()

##Kruskal

print("-----------------Kruskal edges--------------")
res = graphMap.Kruskal()

G = nx.Graph()
for r in res :G.add_edge(r[0], r[1], weight= res[r])
# positions for all nodes
pos = nx.spring_layout(G)  
# nodes
nx.draw_networkx_nodes(G, pos, node_size=100)
# edges
nx.draw_networkx_edges(G, pos,width=3)
# labels
nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')
plt.axis('off')
plt.show()






	


