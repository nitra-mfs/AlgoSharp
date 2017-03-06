"""
TD_intro

"""
import random

#First part: List and Matrix
#Split a list and return the beginning, the end and the median

def splitList(L):
    med = len(L)//2
    return (L[:med],L[med],L[med+1])

#Dichotomy research, return the index of x and if it is not in L return where it sould be 

def binarySearch(L,x,left,right):
    if right <= left:
        return right
    else:
        # med = left+(right-left)//2
        med = (left+right)//2
        if x == L[med]:
            return med
        elif x < L[med]:
            return binarySearch(L,x,left,med)
        else:
            return binarySearch(L,x,med+1,right)

def listSearch(x,L):
    return pos if pos < len(L) and L[pos] == x else -1

#return a list of len = nb fill of val or randint

def buildList(nb,val = None, alea = None):
    l = []
    if val != None or alea == None:
        for i in range(nb):
            l.append(val)
    else:
        for i in range(nb):
            l.append(random.randint(alea[0],alea[1]-1))
    return l
#return an list of list column = nbC , Len = nbL fill of val or randint

def buildMatrix(nbL,nbC,val = None, alea = None):
    M = []
    for l in range(nbL):
        M.append(buildList(nbC,val,alea))
    return M

#Second part: pars
#return a list fill with the content of file

def loadFileToList(file):
    f = open(filename,'r')
    L = f.readlines()
    f.close()
    L = [s.strip() for s in L]
    return L

#return the index of c in L if it doesn't exist, return -1 

def findChar(c,L):
    (i,n) = (0,len(l))
    while(i < n):
        if L[i][0] == c:
            return i
        i+=1
    return -1

def assoc(c,L):
    i = findChar(c,L)
    return L[i][1] if i >= 0 else None

def buildAssocList(filename):
    L = loadFileToList(filename)
    (cpt, l) = (0,[])
    for i in range(len(lines)):
        for j in range(len(line[i])):
            c = lines[i][j]
            if findChar(c,l) == -1:
                L.append((c,l))
            else:
                (c,val) = L[findChar(c,l)]
                L[findChar(c,l)] = (c,val+1)
    return L
