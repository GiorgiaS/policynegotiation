import random
import time
import concurrent.futures
import threading

from PredefSets import PredefSets
from MeanNumber import MeanNumber
from ObjectiveSet import ObjectiveSet
from Algorithms import Algorithms
from Printer import Printer

class IntermediatePolicy():

    def main():
        # Variables
        nPols = 25
        nPPs = 500
        minRet = 30
        maxRet = 365
        predSets = PredefSets()
        algo = Algorithms()
        printer = Printer()

        # Algorithm time:
        time_NSGA3 = 0

        printer.initiateFolders()

        # Set Policies
        # pol = <{prp}, ret, {tp}>
        polPrpList = predSets.getPrpListsPolicy(nPols)
        polTPList = predSets.getTPListsPolicy(nPols)
        polRetList = [] 
        for i in range(nPols):
            polRetList.append(random.randint(minRet, maxRet))

        # Set Privacy Preferences
        # pp = <{prp}, ret, {tp}>
        # Purposes and Thurd Parties must be a subset of those in pol
        ppPrpList = predSets.getPrpListsPP(nPPs)
        ppTPList = predSets.getTPListsPP(nPPs)
        ppRetList = [] 
        for i in range(nPPs):
            ppRetList.append(random.randint(minRet, maxRet))
        
        #####
        # PURPOSE
        #####
        prpReq = 'purpose'
        allPrpLists = predSets.getPowersetPrp()
        # print("IntermediatePolicy.main - Purpose powerset:", allPrpLists)
        # print("IntermediatePolicy.main - Purpose powerset:", type(allPrpLists))
        prpDict = predSets.getPrpDict()
        objPrp = ObjectiveSet(polPrpList, ppPrpList, allPrpLists, prpDict)

        #####
        # THIRD PARTY
        #####
        # i.e., the intermediate set with the smaller value returned by the objective algorithm
        tpReq = 'third-party'
        allTPLists = predSets.getPowersetTP()
        # print("IntermediatePolicy.main - TP powerset:", allTPLists)
        # print("IntermediatePolicy.main - TP powerset:", type(allTPLists))
        tpDict = predSets.getTPDict()
        objTP = ObjectiveSet(polTPList, ppTPList, allTPLists, tpDict)
        
        #####
        # RETENTION
        #####
        meanN = MeanNumber()
        retReq = 'retention'
        
        # Start threads using ThreadPoolExecutor
        st = time.time()
        newPrp = newTP = ''
        newRet = 0
        differencePrp = differenceTP = 0
        PrpResultDict = TPResultDict = {}
        bsPrp = bsTP = 0
        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_prp = executor.submit(algo.computeNSGAIII_Energy, objPrp)
            future_tp = executor.submit(algo.computeNSGAIII_Energy, objTP)
            future_ret = executor.submit(meanN.computeMeanNumber, ppRetList, polRetList)
            
            # Wait for both futures to complete
            differencePrp, newPrp, PrpResultDict, bsPrp = future_prp.result()
            differenceTP, newTP, TPResultDict, bsTP = future_tp.result()
            newRet = future_ret.result()

        time_NSGA3 = time.time()-st
        
        # Print results 
        printer.printSetResults(prpReq, PrpResultDict, bsPrp, differencePrp)
        printer.printSetResults(tpReq, TPResultDict, bsTP, differenceTP)
        printer.printNumResults(retReq, ppRetList, polRetList, newRet)
        


        newPolicy = "<" + str(newPrp) + ", " + str(newRet) + ", " + str(newTP) + ">"
        # print("\nIntermediatePolicy.Main - New Policy (NSGA-III):", newPolicy_NSGAIII)

        # Final result with policies and privacy preferences
        filename = 'Overall_Results'
        printer.printFinalResults(filename, time_NSGA3, newPolicy)
        printer.printPrivacySettings(filename, 'Policies:', polPrpList, polRetList, polTPList)
        printer.printPrivacySettings(filename, 'Privacy Preferences:', ppPrpList, ppRetList, ppTPList)
    

    if __name__ == "__main__":
        main()