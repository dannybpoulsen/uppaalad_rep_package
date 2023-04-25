import models.duqu.case
import models.duqu.duqu.uppaal.output

import tempfile
import os

class Model:
    def __init__ (self):
        self._dir = tempfile.TemporaryDirectory ()
        self._fpath = os.path.join (self._dir.name,"model.xml")
        with  open(self._fpath,"w") as f:
            output = models.duqu.duqu.uppaal.output.Output ()
            f.write(output.output (self._fpath,models.duqu.case.duqu20 ()))
        
    def modelpath (self):
        return self._fpath

    def attacker_actions (self):
        return ["actions"]
