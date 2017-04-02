#tuple and bijection


class Tree:

    def __init__(self, key = None, children = None):
        self.key = key
        if children is not None:
            self.children = children
        else:
            self.children = []

    @property
    def nbChildren(self):
        return len(self.children)

class TreeAsBin:

    def __init__(self,key,child = None,sibling = None):
        self.key = key
        self.child = child
        self.sibling = sibling
'''
def tutoEx1():
    C1 = Tree(3,[Tree(-6),Tree(10)])
    C2 = Tree(8,[Tree(11,[Tree(0),Tree(4)]),Tree(2),Tree(5)])
    C3 = Tree(9)
    return Tree(15,[C1,C2,C3])

T = tutoEx1()

def tutoEx1():
    C1 = TreeAsBin(3,TreeAsBin(-6,None,TreeAsBin(10))]
    C2 = TreeAsBin(8,TreeAsBin(0,None,TreeAsBin(4)),TreeAsBin(2,None,TreeAsBin(5))))
    C3 = TreeAsBin(9)
    C1.sibling = C2
    C2.sibling = C3
    return TreeAsBin(15,C1,None)

TAB = tutoEx1()

'''
