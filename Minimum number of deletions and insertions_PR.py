#Minimum number of Insertions/Removal to convert string1 to srting2.
#Logic is to find the lCS of both string Substract it with lenght of String1 and add it to the (lenght of string2-lcs)

def lcs_string(str1,str2):
    
    """This function finds the longest common subsequence of two string(str1,str2)"""
    dp=[[0 for x in range(len(str2)+1)] for x in range(len(str1)+1)]
    maxx=0

    #print(dp)
    for row in range(len(str1)+1):
        for column in range(len(str2)+1):

            if (row == 0 or column == 0):
                dp[row][column]=0
            else:
                #Character matching in both string
                if(str1[row-1]==str2[column-1]):
                    dp[row][column]=1+dp[row-1][column-1]
                    #print(str1[row-1])
                    if(dp[row][column]>maxx):
                        maxx=dp[row][column]
                        #print("With Match",str1[row-1])
                else:
                    dp[row][column]=max(dp[row-1][column],dp[row][column-1])
    #print(dp)
    return(dp[row][column])

#main part.
if __name__ == "__main__":
    str1="heap"
    str2="pea"
    #Length of longest common subsequence.
    lcs=lcs_string(str1,str2)
    ans=(len(str1)-lcs)+(len(str2)-lcs)
    print(ans)
