import os
from io import StringIO 

class Output:
    def uppaalify (self,name):
        n = name.replace(" ","_").replace("-","_").replace(".","_")
        version = self._names.get (n,0)+1
        self._names[n] = version
        return f"{n}_{version}"
        
        
    def output (self,name,ad):
        self._blocknames =  []
        self._names = {}
        path = os.path.split(os.path.abspath(__file__))[0]
        modelpath = os.path.join (path,"model.xml")
        with open(modelpath,'r') as ff:
            modeltext = ff.read ()
        self._decl = StringIO ()
        self._sys = []
        self._nextatom = 0
        
        ad.visit(self)
        self._decl.seek (0)
        decl = self._decl.read ()
        system = ",".join (self._sys)
        
        return modeltext.replace("#NB#",str(self._nextatom)).replace ("#DECL#",decl+f"system Attacker,{system};")
        
        
    def caseAtom (self,atom):

        
        upp_name = self.uppaalify (atom.getName ())
        actionname = f"actions[{self._nextatom}]"
        prop_name = f"props[{self._nextatom}]"
        block_name = f"{upp_name}_block"
        if (atom.getBlockable ()):
            self._blocknames.append (block_name)
        
        tt_name = f"{upp_name}_tt"
        self._nextatom = self._nextatom + 1
        
        decl = f'''broadcast chan {tt_name}; const bool {block_name} = false;        
{upp_name} = Atom ({prop_name},{actionname},{tt_name},{block_name});

'''
        self._sys.append (upp_name)
        self._decl.write (decl)
        return tt_name
        
    def caseSAND (self,sand):
        upp_name = self.uppaalify (sand.getName ())
        tt_name = f"{upp_name}_tt"
        
        left_tt = sand.getLeft ().visit (self)
        right_tt = sand.getRight ().visit (self)

        decl = f'''broadcast chan {tt_name};
{upp_name} = SAnd ({left_tt},{right_tt},{tt_name});

'''
        self._sys.append (upp_name)
        self._decl.write (decl)
        return tt_name
        
        
    def caseAND (self,sand):
        upp_name = self.uppaalify (sand.getName ())
        tt_name = f"{upp_name}_tt"
        
        left_tt = sand.getLeft ().visit (self)
        right_tt = sand.getRight ().visit (self)

        decl = f'''broadcast chan {tt_name};
{upp_name} = And ({left_tt},{right_tt},{tt_name});

'''
        self._sys.append (upp_name)
        self._decl.write (decl)
        return tt_name
        
    
    
    def caseOR (self,sand):
        upp_name = self.uppaalify (sand.getName ())
        tt_name = f"{upp_name}_tt"
        
        left_tt = sand.getLeft ().visit (self)
        right_tt = sand.getRight ().visit (self)

        decl = f'''broadcast chan {tt_name};
{upp_name} = Or ({left_tt},{right_tt},{tt_name});
'''
        self._sys.append (upp_name)
        self._decl.write (decl)
        return tt_name
        
    
