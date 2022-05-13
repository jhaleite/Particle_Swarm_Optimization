import numpy as np

def Objective_Function(xj):
    
    #########################################################################
    # Here can be implemented any objective function. 
    #########################################################################

    #Rosenbrook function with 2 variables
    fx = np.zeros((len(xj)), dtype=float) 
    for i in range(len(xj)):
            fx[i] = 100*(xj[i][1] - (xj[i][0]**2))**2 + ((1 - xj[i][0])**2)       
    return fx
    
