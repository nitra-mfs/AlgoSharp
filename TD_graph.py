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

def fromGRA(filename):
    file = open(filename,'c')
    directed = 0 != int(file,readline().strip())
    order = int(file.readline().strip())
    G = Graph(order,directed)
    for line in file.readlines():
        line = line.strip().split()
        addEdge(G,int(line[0]),int(line[1]))
    file.close()
    return G

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

def _bfsMat(G,src,M):
    Q = Queue()
    Q = queue.enqueue(src,Q)
    M[src] = -1
    while(not queue.isEmpty(Q)):
        cur = queue.dequeue(Q)
        for dst in range (G.order):
            if (G.adj[cur][dst] > 0 and M[dst] == None):
                queue.enqueue(dst,Q)
                M[dst] = cur

def _bfsAdj(G,src,M):
    Q = Queue()
    Q = queue.enqueue(src,Q)
    M[src] = -1
    while not queue.isEmpty(Q):
        cur = queue.dequeue(Q)
        for dst in G.adjLists[cur]:
            if None == M[dst]:
                queue.enqueue(dst,Q)
                M[dst] = cur


def bfsMath(G,src):
    M = [ None ] * G.order
    _bfsMath(G,src,M)
    for src in range(G.order):
        if M[src] = None:
            _bfsMath(G,src,M)
    return M

def _depthMat(G,src,M):
    for dst in range (G.order):
        if G.adj[src][dst] > 0:
            if M[dst] == None:
                print(src,'->',dst,'covering edge')
                M[dst] = src
                _depthMat(G,dst,M)
            elif M[src] != dst:
                print(src,'->',dst,'back edge')

def depthMat(G,src):
    M = [ None ] * G.order
    M[src] = -1
    _depthMat(G,src,M)
    for src in range (G.order):
        if M[src] == None:
            M[src] = -1
            _depthMat(G,src,M)
    return M

"""
covering edge: pref(src) < pref(dst) < suff(dst) < suff(src)
back     edge: pref(dst) < pref(src) < suff(src) < suff(dst)
forward  edge: pref(src) < pref(dst) < suff(dst) < suff(src)
cross    edge: pref(dst) < suff(dst) < pref(src) < suff(src)

"""

def _depthAdj(G,src,M,cpt,pref,suff):
    #prefix
    cpt += 1
    pref[src] = cpt
    #Iterate
    for dst in G.adjLists[src]:
        if M[dst] == None:
            M[dst] = src
            cpt = _depthAdj(G,src,cpt,pref,suff)
        elif pref[src] < pref[dst]:
            print('forward',src,dst)
        elif suff[dst] == None:
            print('back',src,dst)
        else:
            print('cross',src,dst)
    cpt += 1
    suff[src] = cpt
    return cpt

def depthAdj(G,src):
    M = [ None ] * G.order
    M[src] = -1
    cpt = 0
    pref = [ None ] * G.order
    suff = [ None ] * G.order
    cpt= _depthAdj(G,src,M,cpt,pref,suff)
    for src in range(G.order):
        if M[src] == None:
            M[src] = -1
            cpt += _depthAdj(G,src,M,cpt,pref,suff)
    return M

def _isBiparti(G,src,M):
    for dst in range(G.order):
        if G.adj[src][dst] > 0:
            if M[dst] == None:
                M[dst] = not src
                if not _isBiparti(G,dst,M):
                    return False
            if M[dst] == M[src]:
                return False
    return True

def isBiparti(G):
    M = [ None ] * G.order
    for son in range(G.order):
        M[son] = True
        if not _isBiparti(G,son,M):
            return False
    return True

"""
in one function with bfs
"""

def isBiparti(G):
    M = [ None ] * G.order
    Q = Queue()
    for son in range (G.order):
        M[son] = True
        Q = queue.enqueue(son,Q)
        while(not queue.isEmpty(Q))
            src = queue.dequeue(Q)
            for dst in range(G.order):
                if G.adj[src][dst] > 0:
                    if M[dst] == None:
                        M[dst] = not M[src]
                        queue.enqueue(dst,Q)
                    elif M[dst] == M[src]:
                        return False
        return True

def _isTree(G,src,M):
    b = True
    i = 0
    lenght = len(G.adgjLists(src))
    while(i < lenght and b):
        dst = M[G.adjLists[src][i]]
        if M[dst] == None:
            M[dst] = src
            b = _isTree(G,dst,M)
        elif M[src] != dst:
            b = False
        i += 1
    return b

def isTree(G):
    M = [ None ] * G.order
    M[0] = -1
    b = _isTree(G,0,M)
    i,t = 0,G.order
    while i < t and b:
        b = M[i] != None
        i += 1
    return b

def distance(G,src):
    Q = Queue()
    Q = queue.enqueue((S,0),Q)
    M = [ None ] * G.order
    M[src] = -1
    while not queue.isEmpty(Q):
        (cur,tmp) = queue.dequeue(Q)
        for dst in G.adjLists[cur]:
            if M[dst] = None:
                queue.enqueeu((dst,tmp + 1),Q)
                M[dst] = -1
    return cur,tmp

def diameter(G):
    (s1,a) = distance(G,0)
    (s2,b) = distance(G,s1)
    return b

def _topo(G,src,M,L):
    M[src] = True
    for dst in G.adjLists[src]:
        if not M[dst]:
            _topo(G,dst,M,L)
    #suffix
    L.insert(0,src)

def topo(G,src):
    M = [ False ] * G.order
    L = []
    for src in range(G.order):
        if not M[src]:
            _topo(G,src,M,L)
    return L
