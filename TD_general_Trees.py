


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
