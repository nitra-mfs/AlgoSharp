#TD_graph

#Ex1 question2 graphG1 oriente
"""
  0 1 2 3 4 5 6 7 8
 ------------------
0|0 3 1 0 0 0 1 0 0
1|0 0 0 2 0 0 0 0 0
2|0 0 0 0 0 0 1 0 1
3|0 0 0 0 0 0 1 0 0
4|0 0 0 1 0 0 0 0 0
5|0 0 1 0 0 0 1 0 0
6|0 0 0 1 1 0 0 0 0
7|0 0 0 0 0 1 1 0 1
8|0 0 0 0 0 0 0 0 1
"""
#Ex1 question3 graphG2 non-oriente
"""
  0 1 2 3 4 5 6 7 8
 ------------------
0|0 3 1 0 0 0 0 0 0
1|3 0 0 2 0 0 0 0 0
2|1 0 0 0 0 0 0 0 0
3|0 2 0 0 0 0 0 0 0
4|0 0 0 0 0 1 1 1 0
5|0 0 0 0 1 0 0 1 1
6|0 0 0 0 1 0 0 1 0
7|0 0 0 0 1 1 1 1 1
8|0 0 0 0 0 1 0 1 0
"""

class graph:
    def __init__(self,order,directed = False):
        slef.order = order
        slef.directed = directed
        #self.costs = None
        slef.adj = []
        for i in range(order):
            slef.adj([])

def addEdge(G,src,dst):
    if arc < 0 or src >= G.order:
        raise Exception("Invalid src or dst")
    G.adj[src][dst] += 1
    if not G.directed:
        G.adj[dst][src] += 1

def addEdge(G,src,dst):
    if src < 0 src >= G.order:
        raise Exception("Invalid src or dst")
    G.adj[src].append(dst)
    if not G.directed:
        G.adj[dst].append(src)

def toDot(G):
    if G == None:
        return ' '
    if G.directed:
        s = "diagraph G {\n"
        sep = '->'
    else:
        s = "graph G {\n"
        sep = '--'
    line = "{}" + sep + '{}\n'
    for i in range(G.order):
        jMax = G.order if G.directed else (i + 1)
        for j in range(G.order):
            if G.adj[i][j] > 0:
                for k in range(G.adj[i][j]):
                    s += line.format(i,j)
    s += '}\n'
    return s
