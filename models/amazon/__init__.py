import os

class Model:
    def modelpath (self):
        return os.path.join (os.path.split(os.path.abspath (__file__))[0],"ama2.xml")
