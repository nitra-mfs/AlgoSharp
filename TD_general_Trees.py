
from tree import Tree
from tree import TreeAsBin


def newQueue():
    return queue.Queue()

def isEmpty(q):
    return q.empty()

def enqueue(e, q):
    return q.put(e)

def dequeue(q):
    if not isEmpty(q):
        return q.get()
    else:
        raise Exception ("")

C1 = Tree(3,[Tree(-6),Tree(10)])
C2 = Tree(8,[Tree(11,[Tree(0),Tree(4),Tree(2),Tree(5)])])
C3 = Tree(9)

C = Tree(15,[C1,C2,C3])

T1 = TreeAsBin(3,TreeAsBin(-6,None,TreeAsBin(10)))
T2 = TreeAsBin(8,TreeAsBin(11,TreeAsBin(0,None,TreeAsBin(4)),TreeAsBin(2,None,TreeAsBin(5))))
T3 = TreeAsBin(9)
T1.sibling = T2
T2.sibling = T3

T = TreeAsBin(15,C1,None)

def Size(T):
    if T == None:
        return 0
    else:
        t = 1
        for i in range(T.nbChildren):
            t += Size(T.children[i])
    return n

def SizeTAB(T):
    if T == None:
        return 0
    else:
        n = 1
        child = T.child
        while(child != None):
            n += SizeTAB(child)
            child = child.sibling
        return n

def Height(T):
    if T == None:
        return -1
    else:
        t = -1
        for i in range(T.nbChildren):
            t += max(t,Height(T.children[i]))
        return t + 1

def HeightTAB(T):
    if T == None:
        return -1
    else:
        return max(HeightTAB(T.child) + 1, HeightTAB(T.sibling))

def HeightTABs(T):
    if T == None:
        return -1
    else:
        h = -1
        child = T.child
        while(child != None):
            h = max(h,heightTAB(child))
            child = child.sibling
        return 1 + h

def countLinkandNodes(T):
    if T == None:
        return 0,0
    else:
        nbInt,nbLink = 0,0
        if T.child != None:
            nbInt = 1
        child = T.child
        while(child != None):
            nbLink += 1
            child = child.sibling
            childInt,childLink = countLinkandNodes(child)
            nbInt += childInt
            nbLink += childLink
        return nbInt,nbLink

def averageArity(T):
    nbInt,nbLink = countLinkAndNodes(T)
    if nbInt == 0:
        return 0
    return nbLink/nbInt

def depth(T):
    if T != None:
        #prefix
        if T.nbChildren != 0:
            for i in range(T.nbChildren):
                depth(T.children[i])
                print("inter")
            #depth(T.children[-1])
            print("suffix")

def depthTAB(T,p = None):
    if T != None:
        #prefix
        print(T.key,'prefix')
        depthTAB(T.child,T)
        if T.sibling != None and p != None:
            #inter
            print(p.key,'inter')
            depthTAB(T.sibling,p)
        #suffix
        print(T.key,'suffix')

def depthTab(B):
    if B == None:
        return
    #prefix
    print(B.key,'prefix')
    child = B.child
    while(child != None):
        depthTab(child)
        child = child.sibling
        if child != None:
            #inter
            print(B.key,'inter')
    #suffix
    print(B.key,'suffix')


def breadth(T):
    q = queueQueue()
    queue.enqueue(T,q)
    queue.enqueue(None,q)
    while not queue.isEmpty(q):
        B = queue.dequeue(q)
        if B == None:
            if not queue.isEmpty(q):
                q = queue.enqueue(None,q)
            else:
                for i in range(nbChildren):
                    queue.enqueue(T.children[i],q)


def breadthTAB(T):
    if T == None:
        return
    Q = queue.Queue()
    queue.enqueue(B,Q)
    queue.enqueue(None,Q)
    while not queue.isEmpty(Q):
        B = queue.dequeue(Q)
        if B == None:
            if not queue.isEmpty(Q):
                queue.enqueue(None,Q)
            else:
                child = B.child
                while child != None:
                    queue.enqueue(child,Q)
                    child = child.sibling

def build_vect(A,L):
    L.append(A.key)
    for i in range(A.nbChildren):
        build_vect(A.children[i])
    L.append(A.key)

def build(A):
    L = []
    if A != None:
        build_vect(A,L)
    return L

def same(T,B):
    if T == None or B == None:
        return False
    elif T == None and B == None:
        return True
    elif T.key != B.key:
        return False
    else:
        i = 0
        test = True
        C = B.child
        while(i < T.nbChildren and C != None and test):
            test = same(T.children[i],C)
            C = C.sibling
            i += 1
        return test and i == T.nbChildren and C == None

def TABtoTree(T):
    if T == None:
        return None
    else:
        B = Tree(T.key)
        child = T.child
        while(child != None):
            B.children.append(TABtoTree(child))
            child = child.sibling
        return B

def TreeToTAB(T):
    if T == None:
        return None
    B = TreeAsBin(T.key)
    if (T.nbChildren != 0):
        B.child = TreeToTAB(T.children[0])
        child = B.child
        for i in range(1,T.nbChildren[i]):
            child.sibling = TreeToTAB(T.children[i])
            child = child.sibling
    return B

def Tree2List(B):
    if B == None:
        return ''
    s = '('
    s += str(B.key)
    for child in T.children:
        s += Tree2List(child)
    s += ')'
    return s

def TAB2List(B):
    if B == None:
        return ''
    s ='(' + str(B.key)
    child = T.child
    while(child != None):
        s += TAB2List(child)
        child = child.sibling
    s += ')'
    return s

def TAB2List(B):
    if T == None:
        return ''
    return '(' + str(T.key) + TAB2List(B.child) + ')' + TABtoList(T.sibling)


