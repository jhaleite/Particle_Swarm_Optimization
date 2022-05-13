
from External_Functions import Objective_Function
from PSO_Bib import PSO


obj = PSO(8, 2, 100, -5, 5, 1.5, 2.0, 0.75)

obj.PSO_Optimizer(Objective_Function,'min')

print(obj.Memory_Xj)
