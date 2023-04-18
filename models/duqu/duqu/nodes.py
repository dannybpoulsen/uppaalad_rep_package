from enum import Enum

    

class Node:
    def __init__(self,name = ""):
        self._name = name
        self._blockable = False
        
    def getName (self):
        return self._name

    def setBlockable (self):
        self._blockable = True

    def getBlockable (self):
        return self._blockable
        
class Atom(Node):
    def __init__(self,name):
        super().__init__(name)

    def visit(self,visitor):
        return visitor.caseAtom (self)
    
class Compound(Node):
    def __init__(self,left, right,name=  ""):
        super().__init__(name)
        self._left = left
        self._right = right

    def getLeft (self):
        return self._left

    def getRight (self):
        return self._right

    
        
class SANDNode(Compound):
    def __init__(self,left,right,name = ""):
        super().__init__(left,right,name)

    def visit(self,visitor):
        return visitor.caseSAND (self)

    

class AndNode(Compound):
    def __init__(self,left,right,name =""):
        super().__init__(left,right,name)

    def visit(self,visitor):
        return visitor.caseAND (self)


class OrNode(Compound):
    def __init__(self,left,right,name =""):
        super().__init__(left,right,name)

    def visit(self,visitor):
        return visitor.caseOR (self)

    


class CompoundBuilder:
    def __init__(self,Constr = OrNode,name = ""):
        self._constr = Constr
        self._form = None
        self._name = name
        self._i = 0
        
    def add (self,node):
        if self._form == None:
            self._form = node
        else:
            self._form = self._constr (self._form,node,f"{self._name}_{self._i}")
            self._i = self._i + 1
        return self
     
    def get (self):
        return self._form


def Or (name =""):
    return CompoundBuilder (OrNode,name)

def And (name=""):
    return CompoundBuilder (AndNode,name)

def SAnd (name=""):
    return CompoundBuilder (SANDNode,name)
