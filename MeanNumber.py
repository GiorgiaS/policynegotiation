import os

class MeanNumber:
    def computeMeanNumber(self, userList, spaceList):
        # Compute average number for users
        userAvg = 0
        for ret in userList:
            userAvg += ret
        userAvg = userAvg/len(userList)
        
        # Compute average number for space instance
        spaceAvg = 0
        for ret in spaceList:
            spaceAvg += ret
        spaceAvg = spaceAvg/len(spaceList)
        
        # Compute average result
        avgRes = (userAvg + spaceAvg)/2

        # if not os.path.exists('./output/'):
        #     os.makedirs('./output/')

        # resultF = open('./output/'+filename+'Results.txt', "w")

        # resultF.write("\nBest value: " + str(avgRes))

        # resultF.write("\n\nUsers PPs:")

        # i = 0
        # for pp in userList:
        #     i += 1
        #     # print(i, pp)
        #     resultF.write("\n" + str(i) +  ". " + str(pp))

        # # print("\nSpace Pols:")
        # resultF.write("\n\nSpace Pols:")
        # i = 0
        # for pol in spaceList:
        #     i += 1
        #     # print(i, pol)
        #     resultF.write("\n" + str(i) +  ". " + str(pol))

        
        return avgRes