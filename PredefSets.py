from itertools import chain, combinations
import random
import ast

class PredefSets:

    allPrp = []
    allTP = []
    polPrp = []
    polTP = []
    dataset = './Dataset_AllCompletePolicies.txt'

    def getAllPrp(self):
        return self.allPrp

    def getAllTP(self):
        return self.allTP
    
    def getPolPrp(self):
        return self.polPrp

    def getPolTP(self):
        return self.polTP

    # set the Purpose lists from the dataset
    def setPrpLists(self):
        file = open(self.dataset, "r")
        lines = file.readlines()
        for l in lines:
            l.strip() # remove leading and trailing whitespace
            if 'Purposes:' in l:
                prps = l.split(':', 1)[1].strip()
                # Convert the string to a list.
                prpList = ast.literal_eval(prps)
                if prpList not in self.allPrp:
                    self.allPrp.append(prpList)
            
        # print('PredefSets::setPrpLists list of purposes:')
        # for prp in self.allPrp:
        #     print(prp)
        # print()

    def setTPLists(self):
        file = open(self.dataset, "r")
        lines = file.readlines()
        for l in lines:
            l.strip() # remove leading and trailing whitespace
            if 'Third Parties:' in l:
                tps = l.split(':', 1)[1].strip()
                # Convert the string to a list.
                tpList = ast.literal_eval(tps)
                if tpList not in self.allPrp:
                    self.allTP.append(tpList)

        # print('\nPredefSets::setTPLists list of Third Parties:')
        # for tp in self.allTP:
        #     print(tp)
        # print()
        

    def getPrpListsPolicy(self, listLen):
        self.setPrpLists()
        prps = random.sample(self.allPrp, listLen)
        self.polPrp = prps

        # print('\nPredefSets::getPrpListsPolicy - list of purposes in policies:')
        # for prp in prps:
        #     print(prp)
        # print()

        return prps
    
    # get the Third Party lists from the dataset
    def getTPListsPolicy(self, listLen):
        self.setTPLists()
        tps = random.sample(self.allTP, listLen)
        self.polTP = tps
        return tps
    
    def getPrpListsPP(self, listLen):
        prpList = []
        for i in range(listLen):
            # take 1 random policy
            prp = random.choice(self.polPrp) 
            # get a random subset
            pplen = random.randint(1, len(prp))
            randomPrp = random.sample(prp, pplen)
            # append the random subset the the purposes list
            prpList.append(randomPrp)
            # print('PredefSets::getPrpListsPP - Pol Purpose (superset):', prp)
            # print('PredefSets::getPrpListsPP - PP Purposes:', randomPrp)
        # print('PredefSets::getPrpListsPP - PP Purposes:', prpList)
        return prpList
    
    def getTPListsPP(self, listLen):
        tpList = []
        for i in range(listLen):
            # take 1 random policy
            tp = random.choice(self.polTP) 
            # get a random subset
            pplen = random.randint(1, len(tp))
            randomTP = random.sample(tp, pplen)
            # append the random subset the the purposes list
            tpList.append(randomTP)
            # print('PredefSets::getPrpListsPP - PP Purposes:', randomTP)
        # print('PredefSets::getPrpListsPP - PP Third Party List:', tpList)
        return tpList

    def getPowersetPrp(self):
        # 1. get the list of all elements from the extracted purposes
        prpsList = []
        for prps in self.polPrp:
            for prp in prps:
                if prp not in prpsList:
                    prpsList.append(prp)
        # print('PredefSets::getPowersetPrp All prp:', prpsList)
        
        # Powerset:
        result = list(chain.from_iterable(combinations(prpsList, r) for r in range(len(prpsList) + 1)))
        # print('PredefSets::getPowersetPrp All prp:', result)
        return list(filter(None, result))
    
    def getPowersetTP(self):
        tpsList = []
        for tps in self.polTP:
            for tp in tps:
                if tp not in tpsList:
                    tpsList.append(tp)  
        result = list(chain.from_iterable(combinations(tpsList, r) for r in range(len(tpsList) + 1)))
        # print('PredefSets::getPowersetTP All tp:', result)
        return list(filter(None, result))

    # Choice di pymoo non estrae una tupla, ma un valore numerico. Quindi, al posto di passare il powerset, gli passo un range di valori. 
    # Ad ogni valore, però, deve corrispondere una tupla del powerset. Per questo motivo, costruisco un dizionario a cui associo una chiave numerica ad una tupla.
    def getPrpDict(self):
        prpDict = {}
        powerset = self.getPowersetPrp()
        # print('PredefSets::getPrpDict - powerset:', powerset)
        # print('PredefSets::getPrpDict - Prp powerset:', powerset)
        i = 0
        for prp in powerset:
            # print('PredefSets::getPrpDict - current prp in powerset:', prp)  
            prpDict[i] = set(prp)
            i += 1
        # print('PredefSets::getPrpDict - Prp dictionary:', prpDict)  
        
        return prpDict

    def getTPDict(self):
        tpDict = {}
        powerset = self.getPowersetTP()
        # print('PredefSets::getTPDict - powerset:', powerset)
        # powerset = filter(None, powerset)
        i = 0
        for tp in powerset:
            # print('PredefSets::getTPDict - current tp in powerset:', tp)
            tpDict[i] = set(tp)
            i += 1
            
        return tpDict  