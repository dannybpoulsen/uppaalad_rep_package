import tools
import os
import tempfile
import models.amazon

class Experiment:
    def __init__(self,location):
        self._location = location.subLocation ("amazon")
        with tempfile.TemporaryDirectory () as tdir:
            outpath = os.path.join (tdir,"out.xml")
    
            ad = tools.UppaalAD ()

            attacker_actions = ["guess_password","use_ama_pass","use_password","jam_cam","hack_server","enter_house"]
            for a in attacker_actions:
                ad.addAttackerSymbol (a)
                ad.addAttackerTemplate ("Attacker")
                

                ad.run (models.amazon.Model().modelpath(),outpath)
    
    
                with open (outpath,'r') as ff:
                    model = ff.read ()
                    
                    #replace model descr
                    
    
            self._model = model

    def generate (self):
        self.generateHackNoHack ()
        self.generateAutoLock ()
            
    def generateHackNoHack (self):
        ## We wish to check if system without hacker protection refines a systems with hacker protection

        automata = ["Camera","Resident","House","Attacker","AmazonController","AmazonDelivery","hacker"]
                    
        sysaut = list([f"SYS1{p}" for p in automata])+list([f"SYS2{p}" for p in automata])
                    
        
        instantiated = self._model.replace ("system ;",f"SYS1hacker = SYS1Hacker (false); SYS2hacker = SYS2Hacker (true);  system {','.join (sysaut)};")

        name = "nohack_protection_ref_hackprotection"
        with self._location.makeFile (f"{name}.xml") as ff:
            ff.write (instantiated)

        with self._location.makeFile (f"{name}.q") as ff:
            ff.write ("Pr[<=1000] (<> SYS2Attacker.RefineFail)")


    def generateAutoLock (self):
        ## We wish to check if system with no auto_lock features protection refines a systems with auto_lock

        automata = ["Camera","Resident","House","Attacker","AmazonController","AmazonDelivery","hacker"]
                    
        sysaut = list([f"SYS1{p}" for p in automata])+list([f"SYS2{p}" for p in automata])
                    
        
        instantiated = self._model.replace ("system ;",f"SYS1hacker = SYS1Hacker (false); SYS2hacker = SYS2Hacker (false);  system {','.join (sysaut)};").replace ("const int SYS2ama_forget = 0;","const int SYS2ama_forget = 1;").replace ("const int SYS1ama_forget = 0;","const int SYS1ama_forget = 1;").replace ("const bool SYS1auto_lock = 0;","const bool SYS1auto_lock = 0;").replace ("const bool SYS2auto_lock = 0;","const bool SYS2auto_lock = 1;")
        
        name = "AutoLock"
        with self._location.makeFile (f"{name}.xml") as ff:
            ff.write (instantiated)

        with self._location.makeFile (f"{name}.q") as ff:
            ff.write ("Pr[<=1000] (<> SYS2Attacker.RefineFail)")
    


#with tempfile.TemporaryDirectory () as tdir:
#    outpath = os.path.join (tdir,"out.xml")
#    
#    ad = tools.UppaalAD ()

#    attacker_actions = ["guess_password","use_ama_pass","use_password","jam_cam","hack_server","enter_house"]
#    for a in attacker_actions:
#        ad.addAttackerSymbol (a)
#    ad.addAttackerTemplate ("Attacker")
    

#    ad.run (models.amazon.Model().modelpath(),outpath)
    
    
#    with open (outpath,'r') as ff:
#        model = ff.read ()
    
    #replace model descr
#    automata = ["Camera","Resident","House","Attacker","AmazonController","AmazonDelivery","hacker"]

#    sysaut = list([f"SYS1{p}" for p in automata])+list([f"SYS2{p}" for p in automata])

    
    
 #   print (model.replace ("system ;",f"SYS1hacker = SYS1Hacker (true); SYS2hacker = SYS2Hacker (true);  system {','.join (sysaut)};"))
