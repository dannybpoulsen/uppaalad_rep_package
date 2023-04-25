import os

class Location:
    def __init__ (self,prefixpath):
        self._prefixpath = prefixpath
        os.makedirs (self._prefixpath,exist_ok = True)


    def subLocation (self,name):
        path = os.path.join (self._prefixpath,name)
        return Location (path)

    def makeFile (self,name):
        path = os.path.join (self._prefixpath,name)
        return open (path,'w')
        
