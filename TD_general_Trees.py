from AlgoPy import queue
from AlgoPy.queue import Queue


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
            for i in range(T.nbChildren - 1):
                depth(T.children[i])
                #inter
            depth(T.children[-1])
            #suffix

def depthTAB(T,p = None):
    if T != None:
        #prefix
        print(T.key,'prefix')
        depthTAB(T.child,T)
        #suffix
        print(T.key,'suffix')
        if T.sibling != None && p != None:
            #inter
            print(P.key,'inter')
            depthTAB(T.sibling,p)

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
    q = Queue()
    queue.enqueue(T.q)
    queue.enqueue(None,q)
    while not isEmpty(q):
        B = dequeue(q)
        if B == None:
            if not queue isEmpty(q):
                q = enqueue(None,q)
            else:
                print(B.key,end=' ')
                for i in range(nbChildren):
                    enqueue(T.children[i],q)

def breathTAB(T):
    if T == None:
        return
    Q = Queue()
    queue.enqueue(B,Q)
    queue.enqueue(None,Q)
    while not queue isEmpty(Q):
        B = queue.dequeue(Q)
        if B == None:
            print()
            if not queue.isEmpty(Q):
                queue.enqueue(None,Q)
            else:
                print(B.key,end='')
                child = B.child
                while child != None:
                    queue.enqueue(child,Q)
                    child = child.sibling

