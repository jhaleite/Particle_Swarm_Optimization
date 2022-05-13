
import numpy as np

class PSO:

    def __init__(self, Particles_Number, Variables_Number, Max_Number_Of_Generation_Allowed, Lower_Variables_Bounds, Upper_Variables_Bounds , VelocityCoeficient_CognitivePart, VelocityCoeficient_SocialPart, Inertia_value, wFlag=1):

        # Essential variables

        self.N = Particles_Number
        self.n = Variables_Number
        self.T = Max_Number_Of_Generation_Allowed
        self.Upper_Limit = Upper_Variables_Bounds
        self.Lower_Limit = Lower_Variables_Bounds
        self.w_Flag = wFlag
        self.w = Inertia_value # inertia
        self.c1 = VelocityCoeficient_CognitivePart # celocity coeficient related with the cognitive part
        self.c2 = VelocityCoeficient_SocialPart # celocity coeficient related with the social part

        self.X_j = np.zeros((self.N,self.n),dtype=float) # Variables matrix of the fx function. Each line represents a particle and each collumn represents a variable
        self.V_j = np.zeros((self.N,self.n),dtype=float) # Velocity matrix. Each line represents a particle and each collumn represents a variable of the velocity
        self.fx = np.zeros((self.N), dtype=float) # vector results of the each variables of a particle applied to a function fx
        self.fx_lb = np.zeros((self.N),dtype=float) # vector results of each best local of a particle applied to a function fx
        self.Plb = np.zeros((self.N,self.n),dtype=float) # Matrix of all local best of all swarm
        self.Pgb = np.zeros((self.N,self.n),dtype=float) # Matrix of all gloabl best of all swarm


        self.r1 = np.zeros((self.N),dtype=float) # Random vector of the cognitive part   
        self.r2 = np.zeros((self.N),dtype=float) # Random vector of the social part

        # Memory variables creation

        self.Memory_Xj = []
        self.Memory_Vj = []
        self.Memory_Pgb = []

        # Initializng random swarm

        for i in range(self.N):
            for j in range(self.n):
                if (type(self.Lower_Limit) is int) or (type(self.Lower_Limit) is float): 
                    self.X_j[i][j] = np.random.uniform(self.Lower_Limit, self.Upper_Limit)   
                else:
                    self.X_j[i][j] = np.random.uniform(self.Lower_Limit[i][j], self.Upper_Limit[i][j])

    def PSO_Optimizer(self,Objective_Function, target):

        ##########################################################################################################################################################################
        # MAIN PROGRAM
        ##########################################################################################################################################################################

        #  Calculating fx values

        t = 0 

        while t < self.T:
            
            # Calculation fx
            x = np.copy(self.X_j)
            self.fx = Objective_Function(xj=x)

            # Updating all values of the loval best of the swarm

            for i in range(self.N):
                for j in range(self.n):
                    if t == 0:
                        self.Plb[i][j] = self.X_j[i][j] 
                    else:
                        if self.fx[i] < self.fx_lb[i]:
                            self.Plb[i] = self.X_j[i]

            self.fx_lb = Objective_Function(self.Plb)

            # Updating all values of the global best of the warm

            if target == 'min': # Minimization
                aux_min_fx = min(self.fx) # Assuming that the global best is always the lower value of all swarm
                for i in range(self.N):
                    if self.fx[i] == aux_min_fx:
                        aux_memory_gb = i
                for j in range(self.N):
                    self.Pgb[j] = self.X_j[aux_memory_gb]
                self.Memory_Pgb.append(self.Pgb)
            if target == 'max': # Maximization
                aux_max_fx = max(self.fx) # Assuming that the global best is always the higher value of all swarm
                for i in range(self.N):
                    if self.fx[i] == aux_max_fx:
                        aux_memory_gb = i
                for j in range(self.N):
                    self.Pgb[j] = self.X_j[aux_memory_gb]
                self.Memory_Pgb.append(self.Pgb)

            # Updating the velocity of all particles of the swarm

            self.Memory_Vj.append(np.copy(self.V_j))

            for i in range(self.N):
                self.r1[i] = np.random.uniform(0,1)
                self.r2[i] = np.random.uniform(0,1)
            
            if self.w_Flag == 1:
                self.w = 0.9 - ((t/self.T)*(0.9-0.1))

            Aux_Vj = np.copy(self.V_j)
            for i in range(self.N):
                for j in range(self.n):
                    self.V_j[i][j] = (self.w*float(Aux_Vj[i][j])) + (self.c1*float(self.r1[i])*(self.Plb[i][j] - self.X_j[i][j])) + (self.c2*float(self.r2[i])*(self.Pgb[i][j] - self.X_j[i][j]))

            # Updating particle position 

            Aux_Xj = np.copy(self.X_j)
            self.X_j = Aux_Xj + self.V_j

            # Verify if there is any variables out of the bounds

            for i in range(self.N):
                for j in range(self.n):
                    if (type(self.Lower_Limit) is int) or (type(self.Lower_Limit) is float):
                        if self.X_j[i][j] > self.Upper_Limit:
                            self.X_j[i][j] = self.Upper_Limit
                        if self.X_j[i][j] < self.Lower_Limit:
                            self.X_j[i][j] = self.Lower_Limit
                    else: 
                        if self.X_j[i][j] > self.Upper_Limit[i][j]:
                            self.X_j[i][j] = self.Upper_Limit[i][j]
                        if self.X_j[i][j] < self.Lower_Limit[i][j]:
                            self.X_j[i][j] = self.Lower_Limit[i][j]

            self.Memory_Xj.append(self.X_j)

            t = t + 1

        




