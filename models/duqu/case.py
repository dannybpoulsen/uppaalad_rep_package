import models.duqu.duqu.nodes
import models.duqu.duqu.output


def spear_phishing ():
    target = models.duqu.duqu.nodes.SAnd ("Target downloads and opens word document")
    
    for s in ["Vulnerability in Windows True Type Font","Kernel Mode Access"]:
        target.add (models.duqu.duqu.nodes.Atom (s))
    
    exploit = models.duqu.duqu.nodes.SAnd ("Exploit CVE 2014-4148")    
    exploit.add(target.get ())

    spear = models.duqu.duqu.nodes.SAnd ("Spear phishing")    
    spear.add (exploit.get())

    return spear.get()


def lateral_movement ():
    def gain_domain_access ():
        target = models.duqu.duqu.nodes.SAnd ("Gain Domain Access")
        target.add (models.duqu.duqu.nodes.Atom ("Request TGT"))
        target2 = models.duqu.duqu.nodes.SAnd ("Authenticate withKDC")
        target2.add (models.duqu.duqu.nodes.Atom ("Forge PAC"))
        target.add (target2.get ())
        return target.get ()

    
    def propagate ():
        mid = models.duqu.duqu.nodes.Or ("Propagate_Mid").add(models.duqu.duqu.nodes.Atom ("Remotely install custom MSI on target")).add (models.duqu.duqu.nodes.Atom ("Use task scheduler to instal custom MSI on targe")).get ()
        push_to_domain = models.duqu.duqu.nodes.Or ("Push to domain clients").add (models.duqu.duqu.nodes.Atom ("Basic In-memory remote backdoor")).add (models.duqu.duqu.nodes.Atom ("Full Featuress C And C platform")).get ()
        return models.duqu.duqu.nodes.SAnd ("Propagate").add (mid).add (push_to_domain).get ()
    
    target = models.duqu.duqu.nodes.SAnd ("Lateral Movement")
    target.add (gain_domain_access ())
    target.add (propagate ())

    return target.get ()

def execute_payload ():
    def type_q ():
        sand = models.duqu.duqu.nodes.SAnd ("Type Q")
        for i in ["Replace the current process with malicious exe code","Run thread Asynchornously"]:
            sand.add (models.duqu.duqu.nodes.Atom (i))
        return sand.get ()
    
    def type_k ():
        sand = models.duqu.duqu.nodes.SAnd ("Type K")
        for i in ["Replace the current process with malicious exe code","Block until thread finishes"]:
            sand.add (models.duqu.duqu.nodes.Atom (i))
        return sand.get ()
    
    def type_i ():
        sand = models.duqu.duqu.nodes.SAnd ("Type I")
        for i in ["Currently Running Process","Locate Based on first 4 hashed bytes","Replace process with malicious code"]:
            sand.add (models.duqu.duqu.nodes.Atom (i))
        
        return sand.get ()

    def type_g ():
        sand = models.duqu.duqu.nodes.SAnd ("Type G")
        for i in ["Currently Running Process","Replace process with malicious exe code"]:
            sand.add (models.duqu.duqu.nodes.Atom (i))
        return sand.get ()

    def type_l ():
        return models.duqu.duqu.nodes.Atom ("Type L")
    
    
    target = models.duqu.duqu.nodes.Or ("Execute payload")
    for  i in [type_q,type_k,type_i,type_g,type_l]:
        target.add (i())
    return target.get ()

def install_malware ():
    def make_or (name,subs):
        target = models.duqu.duqu.nodes.Or (name)
 
        for h in subs:
            target.add (models.duqu.duqu.nodes.Atom (h))
        
        return target.get ()
        
    
    target = models.duqu.duqu.nodes.SAnd ("Install Malware")
    target.add (make_or ("Decompress ActionData",["LSJB","LZF","FastZ","LSO"]))
    target.add (make_or ("Decrypt ActionData",["Camellia","AES","XTEA","RC4","Multibyte XOR"]))
    target.add (execute_payload ())
    
    return target.get ()

def main_module ():
    return models.duqu.duqu.nodes.Atom ("Main Module")



def duqu20 ():
    target = models.duqu.duqu.nodes.SAnd ("Duqu 2.0")
    target.add (spear_phishing ())
    target.add (lateral_movement ())
    target.add (install_malware ())
    target.add (main_module ())
    return target.get ()


#tree = duqu20 ()
#dotty = duqu.output.GraphOutput ()
#dotty.output ("H",tree)

#g = duqu.uppaal.output.Output  ()    
#g.output ("H",tree)
                
