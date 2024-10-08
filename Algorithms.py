from concurrent.futures import ThreadPoolExecutor
# Algorithms imports
from pymoo.algorithms.moo.nsga3 import NSGA3
from pymoo.optimize import minimize
from pymoo.util.ref_dirs import get_reference_directions


class Algorithms():

    ##############
    #            #
    #  NSGA-III  #
    #            #
    ##############

    def assessObjectiveFunction(self, problem):
        ref_dirs = get_reference_directions("energy", 4, 90)
        # print("IntermediatePolicy - Energy - len(ref_dirs):",len(ref_dirs))
        algorithm = NSGA3(ref_dirs = ref_dirs)
        # algorithm = NSGA3(pop_size=300, ref_dirs = ref_dirs)
        # print("NSGA3-RefLen = ", len(ref_dirs))
        # algorithm = NSGA3(pop_size = 92, ref_dirs = ref_dirs) # population should be equal or greater than len(ref_dirs)

        res = minimize(problem, 
                    algorithm,
                    ("n_gen", 100),
                    seed = 42,
                    # verbose = True
                    )
        best_solution = res.F
        return best_solution
        
    ########
    # ENERGY Reference Directions
    ########
    def computeNSGAIII_Energy(self, problem):
        best_solution = []
        
        with ThreadPoolExecutor() as executor:
            thread = executor.submit(self.assessObjectiveFunction, problem)
            best_solution = thread.result()
        
        # print("Results:", problem.results)

        # energyF = open('./output/NSGA-III/energy/'+filename+'energyResults.txt', "w")
        
        # print("Best objective function values:\n", best_solution)
        
        # energyF.write("Best objective function values:\n" + str(best_solution))

        bestSolutionDict = {}
        # print("Algorithms.computeNSGAIII_Energy - bestValue initial value:", bestValue)
        # resultF = open('./output/algoritm.txt', "a")
        # resultF.write('\n\nProblem: ' + str(problem))
        for bs in best_solution:
            keyBS = round(bs[0] + bs[1] + bs[2] + bs[3], 8)
            # print("Algorithms.computeNSGAIII_Energy - current bs:", bs)
            bestSolutionDict[keyBS] = problem.results[keyBS]
            # if keyBS < bestValue:
            #     bestValue = keyBS
        #     print("Algorithms.computeNSGAIII_Energy - bestValue current value:", bestValue)
        # print("Algorithms.computeNSGAIII_Energy - bestValue final value:", bestValue)

        # The best solution is that with currentDifference = 0
        # So, we start with difference = 1
        difference = 1
        keyBS = 0
        for bs in best_solution:
            difU = round(bs[0] - bs[1], 8)
            difS = round(bs[2] - bs[3], 8)
            currentDifference = abs(difU - difS)
            if (abs(1 - currentDifference)) > (abs(1 - difference)):
                difference = currentDifference
                keyBS = round(bs[0] + bs[1] + bs[2] + bs[3], 8)
                
            # resultF.write('\nbest solution: ' + str(bestSolutionDict[keyBS]) + ': ' + str(bs) + ' currentDifference: ' + str(currentDifference) + ' current difference: ' + str(difference))

        # energyF.write("\n\nBest (= smallest) value: " + str(bestValue) + " => " + str(bestSolutionDict[bestValue]))

        # energyF.close()
        
        return difference, bestSolutionDict[keyBS], bestSolutionDict, keyBS
