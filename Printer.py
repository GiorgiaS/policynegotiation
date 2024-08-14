import os 

class Printer:
    def initiateFolders(self):
        if not os.path.exists('./output/'):
            os.makedirs('./output/')    
        
    def printSetResults(self, filename, resultDict, key, difference):
        objF = open('./output/'+filename+'.txt', "w")
        objF.write("Best Solutions:")
        i = 0
        for bs in resultDict:
            i += 1
            objF.write("\n" + str(i) + ". " + str(bs) + " => " + str(resultDict[bs]))
            
        objF.write("\n\nFinal best solution: " + str(resultDict[key]) + " (difference : " + str(difference) + ")")
        objF.close()
        
    def printNumResults(self, filename, ppList, polList, newVal):
        resultF = open('./output/'+filename+'Results.txt', "w")
        resultF.write("Privacy Preferences:")
        i = 0
        for n in ppList:
            i += 1
            # print(i, pp)
            resultF.write("\n" + str(i) +  ". " + str(n))
        resultF.write('\n')
        resultF.write("\nPolicies:")
        i = 0
        for n in polList:
            i += 1
            # print(i, pp)
            resultF.write("\n" + str(i) +  ". " + str(n))
        
        resultF.write('\n\nFinal best solution: ' + str(newVal))
        resultF.close()
        
    def printPrivacySettings(self, filename, category, prpList, retList, tpList):
        resultF = open('./output/' + filename + '.txt', "a")
        
        resultF.write("\n\nList of " + category + '\n') # category = Policies or Privacy Preferences
        for i in range(len(prpList)): # len(prpList) = len(tpList) = len(retList)
            pol = '<' + str(prpList[i]) + ', ' + str(retList[i]) + ', ' + str(tpList[i]) + '>'
            resultF.write(pol + "\n")
        
        resultF.close()
            
    def printFinalResults(self, filename, time, newPol):
        resultF = open('./output/' + filename + '.txt', "w")
        resultF.write("Intermediate Policy:" + newPol)
        resultF.write("\nComputation time:" + str(time))
        
        resultF.close()