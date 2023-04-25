import experiments.amazon
import experiments.duqu
import tools.location

loc = tools.location.Location ("./out")

experiments = [experiments.amazon.Experiment (loc),experiments.duqu.Experiment (loc)]
for e in experiments:
    e.generate ()



