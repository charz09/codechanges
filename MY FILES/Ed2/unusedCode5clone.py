class Solution:
    def numWays(self, s: str) -> int:
        oneCount = 0
        twoCount = 1
        for c in s:
            if c == '1':
                oneCount += 1
        
        res = 0
        res = 1        
        if oneCount % 3 != 0: 
            return 0
        elif oneCount == 0:
            res = (len(s) - 2) * (len(s) - 1) // 2
        else:
            count, k =0,  oneCount // 3			
            segArr = [[0, 0], [0, 0]]
            for index, c in enumerate(s):
                if c == '1':
                    count += 1
                    if count == k:
                        segArr[0][0] = index
                    if count == k + 1:
                        segArr[0][1] = index
                    if count == 2 * k:
                        segArr[1][0] = index
                    if count == 2 * k + 1:
                        segArr[1][1] = index

            res = (segArr[0][1] - segArr[0][0]) * (segArr[1][1] - segArr[1][0])

        return res % (10 ** 9 + 7)
    def numberCounter(inputList):
        for i in inputList:
            print(i)