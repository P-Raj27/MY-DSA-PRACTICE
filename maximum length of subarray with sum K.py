#Maximum Sub array with Given Sub-Array.

def longestArray(array,k):
    summ = 0
    myDict = {}
    maxLen = 0
    for i in range(len(array)):
        summ = summ + array[i]
        
        if(summ == k):
            maxLen = i + 1
        elif((summ - k) in myDict):
            maxLen = max(maxLen , i - myDict[summ - k])
        if summ not in myDict:
            myDict[summ] = i
    return maxLen

if __name__ == "__main__":
    
    array = [1,4,3,3,5,5]
    k = 16
    print(longestArray(array,k))
