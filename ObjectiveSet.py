from multiprocessing.pool import ThreadPool
from pymoo.core.problem import ElementwiseProblem
import os

# pool = ThreadPool(8)

class ObjectiveSet(ElementwiseProblem):
    results = {}
    pps = []
    pols = []
    prpDict = {}
 
    def __init__(self, polLists, ppLists, allSets, prpDict):
        # print("ObjectiveSet.__init__ - polLists:", polLists)  # Debug print
        # print("ObjectiveSet.__init__ - ppLists:", ppLists)
        self.pps = ppLists
        self.pols = polLists
        self.prpDict = prpDict
        super().__init__(n_var=1, # newSet key
                         n_obj = 4, # 2 for users and 2 for space instance
                         xl = 0,
                         xu = len(allSets) - 1 ,  # or 2?
                         vtype = int
                         )
         
    def jDist(self, newSet, set):
        intersection = len(newSet.intersection(set))
        union = len(newSet.union(set))
        if intersection == 0:
            # print("User.jDist - intersection = 0")
            return 1 - 0
        if union == 0:
            # print("User.jDist - union = 0")
            return 1
        jDist = 1 - (intersection/union)
        # print("User.jDist - union = 0")
        return jDist

    def summation(self, newSet, sets):
        sum = 0
        for set in sets:
            sum += self.jDist(newSet, set)
        # print("User.summation - sets:", sets, "sum:", sum)
        return sum

    def _evaluate(self, vars, out, *args, **kwargs):
        # Constants
        w1 = 0.7
        w2 = 0.3

        # print ("ObjectivePurpose._evaluate - PPS:", self.pps)
        # Common variables
        newSetKey = int(round(vars[0]))  # Use the key instead of directly accessing the set
        newSet = self.prpDict[newSetKey]
        # print("ObjectivePurpose._evaluate - newSet (", newSetKey, "):", newSet)
    
            
        # Users variables
        UE = []
        UU = []
        UF = []
        for prp in self.pps:
            if set(prp) == newSet: 
                UE.append(prp)
            elif set(newSet).issubset(prp): # it means the user has to provide fewer data
                UF.append(prp)
            else: # if prp is different from newSet or if prp is a subset of newSet.
                UU.append(prp)
                
        # if UU:
        #     print("User._evaluate - UUnfav:", UU)
        # if UE:
        #     print("User._evaluate - UEqual:", UE)
        # if UF:
        #     print("User._evaluate - UFav:", UF)            

        # Space variables
        SE = []
        SU = []
        SF = []
        
        for prp in self.pols:
            if set(prp) == newSet: 
                SE.append(prp)
            elif set(prp).issubset(set(newSet)): 
                SF.append(prp)
            else: 
                SU.append(prp)
                
        # if SU:
        #     print("SpaceInstance._evaluate - SUnfav:", SU)
        # if SE:
        #     print("SpaceInstance._evaluate - SEqual:", SE)
        # if SF:
        #     print("SpaceInstance._evaluate - SFav:", SF)  

        # User Objective functions
        if UF and UE:
            f1 = 1 - (1/len(UF) * self.summation(newSet, UF) * w1 + len(UE)/len(self.pps) * w2) # maximise (it is "-" because of pymoo: each objective function is supposed to be minimized)
        elif UF and not UE:
            f1 = 1 - (1/len(UF) * self.summation(newSet, UF))
        elif not UF and UE:
            f1 = 1 - len(UE)/len(self.pps)
        else: 
            f1 = 0 # if no pp is favoured, then this value is 1 to denote the maximum distance
            
        if UU:
            f2 = 1/len(UU) * self.summation(newSet, UU) # minimise
        else:
            f2 = 0 # is no pp is unfavored, this value is 0 to denote the minimum distance
        
        # print("ObjectiveSet._evaluate - user minimise (maximise):", f1)
        # print("ObjectiveSet._evaluate - user minimise:", f2)
        
        # Space Objective functions
        if SF and SE:
            f3 = 1 - (1/len(SF) * self.summation(newSet, SF) * w1 + len(SE)/len(self.pols) * w2) # maximise (it is "-" because of tpymoo: see README.txt)
        elif SF and not SE:
            f3 = 1 - (1/len(SF) * self.summation(newSet, SF))
        elif not SF and SE:
            f3 = 1 - len(SE)/len(self.pols)
        else: 
            f3 = 0 # if no pp is favoured, then this valSE is 1 to denote the maximum distance
            
        if SU:
            f4 = 1/len(SU) * self.summation(newSet, SU) # minimise
        else:
            f4 = 0 # is no pp is unfavored, this valSE is 0 to denote the minimum distance
        
        # print("ObjectiveSet._evaluate - space minimise (maximise):", f3)
        # print("ObjectiveSet._evaluate - space minimise:", f4)
    
        # Without weight
        out["F"] = [f1, f2, f3, f4]
        resultKey = round((f1+f2+f3+f4), 8)

        self.results[resultKey] = newSet
        
        # print("\n")

        
