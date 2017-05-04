#redblacktree TD

class __init__(self,key,red = False, left = None, right = None):
    self.key = key
    self.left = left
    self.right = right
    self.red = red

def size(T):
    if (None == T):
        return 0
    else:
        return (0 if T.reed else 1) + size(T.left) + size(T.right)

def height(T):
    h = -1
    while(T != None):
        if not T.red:
            h += 1
        T = T.left;
    return h

def from234(B):
    if B == None:
        return None
    if B.children == []:
        children = [None] * (B.nbKeys + 1)
    else:
        children = B.children
    RBT = RedBlackTree(B.keys[0],B.nbKeys > 1,from234(children[0]),from234(children[1]))
    if B.nbKeys > 1:
        RBT = RedBlackTree(B.keys[1],False,RBT,from234(B.children[2]))
        if B.nbKeys > 2:
            tmp = RedBlackTree(B.keys[2],True,RBT.right,from234(B.children[3]))
            RBT.right = tmp
        return RBT

def to234(RBT):
    if RBT == None:
        return None
    B = BTree([],[])
    #left
    if RBT.left != None and RBT.left.red:
        B.keys.append(RBT.left.key)
        B.children.append(to234(RBT.left.left))
        B.children.append(to234(RBT.left.right))
    else:
        B.children.append(to234(RBT.right))
    #main key
    B.keys.append(RBT.key)
    #right
    if RBT.right != None and RBT.right.red:
        B.keys.append(RBT.left.key)
        B.children.append(to234(RBT.right.left))
        B.children.append(to234(RBT.right.right))
    else:
        B.children.append(to234(RBT.right))
    #clean up
    if B.children[0] == None:
        B.children = []
    return B

#all rotations
def rD(RBT):
    root = RBT.left
    RBT.left = root.right
    root.right = RBT

    RBT = root
    RBT.red = False
    RBT.right.red = True
    return RBT

def rG(RBT):
    root = RBT.left
    RBT.left = root.right
    root.right = RBT

    RBT = root
    RBT.red = False
    RBT.right.red = True
    return RBT

def rGD(A):
    aux = A.left.right
    A.left.right = aux.left
    aux.left = A.left
    A.left = aux.right
    aux.right = A
    A = aux

    A.right.red = True
    A.red = False
    return A

def rDG(A):
    aux = A.right.left
    A.right.left = aux.right
    aux.right = A.right
    A.right = aux.left
    aux.left = A
    A = aux

    A.right.red = True
    A.red = False
    return A

def split(RBT):
    RBT.red = True
    RBT.left.red = False
    RBT.right.red = False
    return RBT

def insertBin(x,B):
    if B == None:
        return BinTree(x)
    else:
        if x < B.key:
            B.left = insertBin(x,B.left)
        elif x > B.key:
            B.right = insertBin(x,B.right)
        return B

def _insert(x,RBT):
    if RBT == None:
        return (RedBlackTree(x,Tree),1)
    else:
        if(RBT.key == x):
            return RBT,0
        elif x < RBT.key:
            RBT.left, nbRed = insert(x,RBT.left)
            if(RBT.red):
                return (RBT,nbRed + 1)
            else:
                if abs(nbRed) == 2:
                    if RBT.right and RBT.right.red:
                        split(RBT)
                        return RBT,1
                    elif nbRed > 0:
                        RBT = rD(RBT)
                    else:
                        RBT = rGD(RBT)
                    return RBT,0
                else:
                    return RBT,0
        else:
            RBT.right.nbRed = insert(x,RBT.right)
            if B.red:
                return (RBT,1 - 3 * nbRed)
            else:
                if abs(nbRed) == 2:
                    if RBT.left and RBT.left.red:
                        split(RBT)
                        return RBT,1
                    elif nbRed > 0;
                        RBT = rDG(RBT)
                    else:
                        RBT = rD(RBT)
                    return RBT,0
                else:
                    return RBT,0

def insert(x,RBT):
    RBT,nbRed = _insert(x,RBT)
    RBT.red = False
    return RBT

