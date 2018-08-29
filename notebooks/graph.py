import igraph
from igraph import *


g = Graph(directed=True)
g.add_vertices(4)
g.vs["name"]=["GO:1234567","GO:6789056","GO:5674321",'GO:9422630']
print g.vs[0]["name"]
g.es["weight"]=1
g['GO:1234567','GO:6789056']=1
g['GO:6789056','GO:9422630']=1
g['GO:9422630','GO:5674321']=1
g['GO:6789056','GO:5674321']=5
print g.is_weighted()
print g.es["weight"]
weight=g.es["weight"]
print weight
print g.degree(mode="in") 
print g.shortest_paths_dijkstra(source="GO:1234567", target="GO:5674321", weights=weight, mode=OUT)
val=g.shortest_paths_dijkstra(source="GO:1234567", target="GO:5674321", weights=weight, mode=OUT)
print val[0][0]