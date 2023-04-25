import tools
import os
import tempfile
import models.duqu

class Experiment:
    def __init__(self,location):
        self._location = location.subLocation ("duqu")
        with tempfile.TemporaryDirectory () as tdir:
            outpath = os.path.join (tdir,"out.xml")
            model = models.duqu.Model()
            
            
            ad = tools.UppaalAD ()
            
            
            attacker_actions = []
            for a in model.attacker_actions():
                ad.addAttackerSymbol (a)
            ad.addAttackerTemplate ("Attacker")
                
            ad.run (model.modelpath(),outpath)
            
    
            with open (outpath,'r') as ff:
                modeltext = ff.read ()
                    
                    #replace model descr
                    
    
            self._model = modeltext

    def generate (self):
        with self._location.makeFile (f"duqu.xml") as ff:
            ff.write (self._model)
        
    
            
        
