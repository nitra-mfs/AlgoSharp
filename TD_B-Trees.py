

class BTree:

    degree = None #va être defini pour toutes les instances de Btree

    def __init__(self,keys=None,children=None):
        self.keys = keys if keys else []
        self.children=children if children else []

    @property

    def nbKeys(self):
        return len(self.keys)

def  _rangeBTree(B,inf,sup,L):
    for i in range(B.keys):
        if B.children != []:
            _rangeBTree(B.children[i],inf,sup,L)
        if B.keys[i] >= inf and B.keys[i] <= sup:
            L.append(B.keys[i])
    if B.children != []:
        _rangeBTree(B.children[-1],inf,sup,L)

def _rangeBTree(B,inf,sup,L):
    if B.children != []:
        
        i = 0
        while i < B.nbKeys and B.keys[i] < inf:
            i += 1
        while i < B.nbKeys and B.keys[i] <= sup:
            _rangeBTree(B.children[i],inf,sup,L)
            L.append(B.keys[i])
            i += 1
        _rangeBTree(B.children[i],inf,sup,L)


        #for i in range(B.keys):
           # _rangeBTree(B.children[i],inf,sup,L)
          #  if B.keys[i] >= inf and B.keys[i] <= sup:
         #       L.append(B.keys[i])
       # _rangeBTree(B.children[-1],inf,sup,L)
    else:
       # for i in range(B.keys):
            #if B.keys[i] >= inf and B.keys[i] <= sup:
                # L.append(B.keys[i])
        i = 0
        while i < B.nbKeys and B.keys[i] < inf:
            i += 1
        while i < B.nbKeys and B.keys[i] <= sup:
            L.append(B.keys[i])
            i += 1

def rangeBTree(B,inf,sup):
    L = []
    if B != None:
        _rangeBTree(B,inf,sup,L)
    return L

def minBTree(B):
    for i in range(B.Keys):
        if B.children != []:
            minBTree(B.children[i])



