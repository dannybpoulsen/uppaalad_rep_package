import logging
import os
import subprocess
from zipfile import ZipFile


def unzip (path,unzippath):
    logging.info (f"Unzipping {path} too {unzippath}") 
    zf = ZipFile(path, 'r')
    zf.extractall(unzippath)
    zf.close()
    
    
def compile (path):
    builddir = os.path.join (path,"build")
    binpath = os.path.join (builddir,"bin","main")
    if not os.path.exists (binpath):
        
        os.makedirs (builddir,exist_ok = True)
        logging.warning (f"Compiling {path} in {builddir}") 
        subprocess.run (["cmake",".."],cwd = builddir)
        subprocess.run (["make"],cwd = builddir)
    return binpath 

    
def unzipAndCompile ():
    path = os.path.split(os.path.abspath (__file__))[0]
    unzippath = os.path.join (path,"uppaalad")
    zippath = os.path.join (path,"uppaalad.zip")
    
    unzip (zippath,unzippath)
    return compile (unzippath)

class UppaalAD:
    def __init__(self):
        self._path = unzipAndCompile ()
        self._attackertemplates = []
        self._attackersymbols = []

    def addAttackerTemplate (self,att):
        self._attackertemplates.append (att)

    def addAttackerSymbol (self,symb):
        self._attackersymbols.append (symb)

    def run (self,input="input.xml",output = "out.xml"):
        params = [self._path,"--model",input,"-o",output]
        for a in self._attackertemplates:
            params.append ("-a")
            params.append (a)

        for a in self._attackersymbols:
            params.append ("-s")
            params.append (a)
        
        subprocess.run (params)

