import graphviz

class GraphOutput:
    def output (self,name,ad):
        self._graph =  graphviz.Digraph(name)
        ad.visit (self)
        self._graph.render ()
        
    def caseAtom (self,atom):
        node = self._graph.node (str(atom),atom.getName ())
        return str(atom)

    def caseSAND (self,sand):
        left = sand.getLeft().visit (self)
        right = sand.getRight().visit (self)
        self._graph.node (str(sand),sand.getName ())
        self._graph.edge (left,str(sand),arrowhead="dot")
        self._graph.edge (right,str(sand),arrowhead="dot")
        return str(sand)
        
        
    def caseAND (self,sand):
        left = sand.getLeft().visit (self)
        right = sand.getRight().visit (self)
        self._graph.node (str(sand),sand.getName ())
        self._graph.edge (left,str(sand),arrowhead="normal")
        self._graph.edge (right,str(sand),arrowhead="normal")
        return str(sand)
        
    
    
    def caseOR (self,sand):
        left = sand.getLeft().visit (self)
        right = sand.getRight().visit (self)
        self._graph.node (str(sand),sand.getName ())
        self._graph.edge (left,str(sand),arrowhead="none")
        self._graph.edge (right,str(sand),arrowhead="none")
        return str(sand)
        
    


if __name__ == "__main__":
    import nodes
    g = GraphOutput  ()    
    atom = nodes.Atom ("HH")
    atom2 = nodes.Atom ("HH2")
    
    compound = nodes.SAnd ()
    compound.add (atom)
    compound.add (atom2)
    g.output ("H",compound.get())
    
    
