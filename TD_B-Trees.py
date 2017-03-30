

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
    if B.children == []:
        return B.keys[0]
    else:
        return minBTree(B.children[0])

def maxBTree(B):
    if B.children == []:
        return B.keys[-1]
    else:
        return maxBTree(B.children[-1])

def maxIter(B):
    while(B.children != []):
        B = B.children[-1]
    return B.keys[-1]

def _binarySearchPos(L,x,left,right):
    if right <= left:
        return right
    else:
        med = left +  (right - left)//2
        if x == L[med]
            return med
        elif x < L[med]:
            return binarySearch(L,x,left,med)
        else:
            return binarySearch(L,x,med+1,right)

def binarySearchPos(L,x):
    return _binarySearchPos(L,x,0,len(L))

def search(B,x):
    if  B == None:
        return None
    else:
        tmp = binarySearchPos(B.keys,x)
        if tmp < B.nbKeys and B.keys[i] == x:
                return (B, tmp)
        else:
            if B.children != []:
                return search(B.children[i],x)
            else:
                return None



def BTree2List(B):
    if B != None:
        s = '(<'
        res += str(B.keys[0])
        for i in range(1,len(B.keys)):
            res += ','
            res += str(B.keys[i])
        res += '>' 
        for j in range(B.children):
            res += BTree2List(B.children[j])
        res += ')'
        return str

'''
insert
'''

def splitBTree(B,n):
    mid = BTree.degree - 1
    L = B.children[n]
    R = BTree()
    (L.keys,x,R.keys) = (L.keys[mid],L.keys[mid],L.key[mid + 1])
    if L.children != []:
        (L.children,R.children) = (L.children[:mid+1],L.children[mid+1:])
    '''
    B.keys = B.keys[:n] + [x] + B.keys[n:]
    B.children = B.children[:n+1] + [R] + B.children[n+1:]
    '''
    B.keys.insert(n,x)
    B.children.insert(n + 1, R)

def fromList(s, i = 0):
    if i < len(s) and s[i] == '(':
        i = i + 2 
        B = BTree()
        while(s[i] != '>'):
            key = ' '
            while not (s[i] in ',>'):
                key += s[i]
                i += 1
                B.keys.append(int(key))
                if s[i] == ',':
                    i += 1
        i += 1
        B.children = []
        while s[i] != ')':
            (C,i) = _fromList(s,i)
            B.children.append(C)
        i = i + 1
        return (B,i)
    else:
        return None

def fromList(s,d):
    BTree.degree = d
    (B,i) = _fromList(s)
    return B

def _insert(B,x):
    i = binarySearchPos(B.keys,x)
    if i < B.nbKeys and B.keys[i] == x:
        return False
    elif B.children == []:
        B.key.insert(i,x)
        return True
    else:
        if B.children[i].nbKeys == BTree.degree * 2 - 1:
            if B.children[i].keys[BTree.degree - 1] = x:
                return False
            if B.keys[i] < x:
                i += 1
        return _insert(B.children[i],x)

def insert(B,x):
    if B == None:
        return BTree([x])
    else:
        if B.nbKeys == 2*BTree.degree - 1:
            R = BTree([],[B])
            split(R,0)
            B = R
        _insert(B,x)
    return B

'''
Suppression

'''

def leftRotation(B,i):
    L = B.children[i]
    R = B.children[i + 1]
    L.append(B.keys[i])
    B.keys[i] = R.key.pop(0)
    if R.children != []:
        L.children.append(R.children.pop(0))

def rightRotation(B,i):
    L = B.children[i - 1]
    R = B.children[i]
    R.keys.insert(0,B.keys[i - 1])
    B.keys[i - 1] = L.keys.pop()
    if L.children != []:
        R.children.insert(0,L.children.pop())

def merge(B,i):
    L = B.children[i]
    R = B.children[i + 1]
    L.keys.append(B.keys.pop(i))
    L.keys += R.keys
    if R.children != []:
        L.children += R.children
    B.children.pop(i + 1)


def _delete(B,x):
    pos = binarySearchPos(B.keys,x)
    if B.children:
        if pos < B.nbKeys and x == B.keys[pos]:
            if B.children[pos].nbKeys > B.children[pos + 1].nbKeys:
                B.keys[pos] = maxBTree(B.children[pos])
                _delete(B.children[pos], B.keys[pos])
            elif B.children[pos + 1].nbKeys > BTree.degree - 1:
                B.keys[pos] = minBTree(B.children[pos + 1])
                _delete(B.children[pos + 1],B.keys[pos])
            else:
                merge(B,pos)
                _delete(B.children[pos],x)
        else:
            if B.children[pos].nbKeys == BTree.degree - 1:
                if pos > 0 and B.children[pos - 1].nbKeys > BTree.degree - 1:
                    rightRotation(B,pos)
                elif pos < B.nbKeys and B.children[pos + 1].nbKeys > BTree.degree - 1:
                    leftRotation(B,pos)
                else:
                    pos = min(pos,B.nbKeys - 1)
                    merge(B,pos)
                _delete(B.children[pos],x)
    else:
        if pos < B.nbKeys and x == B.keys[pos]:
            B.keys.pop(pos)


def delete(B,x):
    if B != None:
        _delete(B,x)
        if B.nbKeys > 0:
            return B
        elif B.children:
            return B.children[0]
    return None


