'''
Two Sum
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9

Output: index1=1, index2=2
'''
class TwoSumA:

    def __init__(self,tempList,target):
        
        self.tempList = tempList
        self.target = target

    def findIndex(self):
        
        result = []
        indexA = 0
        indexB = 0
        if len(self.tempList) <= 1:
            print('List length is not valid.')
       
        else:
            for i in range(len(self.tempList)-1):
                for j in range(i+1,len(self.tempList)):
                    if self.tempList[i] + self.tempList[j] == self.target:
                        result.append((i,j))
            return result
        
    def printIndex(self,indexList):
        
        if indexList:
            for index in indexList:
                print('index1 = {},index2 = {},target = {}.'.format(index[0],index[1],self.target))
        else:
            print('given list {} not found two item  sum is {}.'.format(self.tempList,self.target))


if __name__ == '__main__':

    tempList = [2,7,11,15]
    targetA = 9
    targetB = 10
    twosum = TwoSumA(tempList,targetA)
    indexList = twosum.findIndex()
    twosum.printIndex(indexList)
    twosumB = TwoSumA(tempList,targetB)
    indexList = twosumB.findIndex()
    twosumB.printIndex(indexList)

            
        
        
