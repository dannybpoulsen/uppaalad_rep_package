import tools
import os
import tempfile

model = os.path.join (os.path.split(os.path.abspath (__file__))[0],"models","ama2.xml")

with tempfile.TemporaryDirectory () as tdir:
    outpath = os.path.join (tdir,"out.xml")
    
    ad = tools.UppaalAD ()

    attacker_actions = ["guess_password","use_ama_pass","use_password","jam_cam","hack_server","enter_house"]
    for a in attacker_actions:
        ad.addAttackerSymbol (a)
    ad.addAttackerTemplate ("Attacker")
    

    ad.run (model,outpath)
    with open (outpath,'r') as ff:
        model = ff.read ()
    
    #replace model descr
    automata = ["Camera","Resident","House","Attacker","AmazonController","AmazonDelivery","hacker"]

    sysaut = list([f"SYS1{p}" for p in automata])+list([f"SYS2{p}" for p in automata])

    
    
    print (model.replace ("system ;",f"SYS1hacker = SYS1Hacker (true); SYS2hacker = SYS2Hacker (true);  system {','.join (sysaut)};"))
