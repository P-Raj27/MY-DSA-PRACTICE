#Shortest SuperSequence.
#Logic used here is what if we calculate the LCS(Longest Common Subsequence) of both the string and add it to the (length of string1-lcs)+(length of string2-lcs).
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
    return(dp,dp[row][column])

#main part.
if __name__ == "__main__":
    str1 = "acbbcccaa"
    str2 = "bbbcaaaaa"
    dp,lcs = lcs_string(str1,str2)
    len1=len(str1)-lcs
    len2=len(str2)-lcs
    ans=len1+len2+lcs
    print(ans)
    string=""
    i=len(str1)
    j=len(str2)
    
    
    #Printing of Subsequence.
    while (i>0 and j>0):
        print("hi")
        if(str1[i-1]==str2[j-1]):
            string=str1[i-1]+string
            i=i-1
            j=j-1
        elif(dp[i-1][j]>dp[i][j-1]):
            string=str1[i-1]+string
            print(i)
            i=i-1
        else:
            string=str2[j-1]+string
            print(i)
            j=j-1
    print(string)
    print(i,j)
    if(i>0):
        for k in range(i,0,-1):
            print("i here is=",i)
            print(str1[i-1])
            string=str1[k-1]+string
    else:
        for r in range(j,0,-1):
            string=str2[k-1]+string
            
                
    print(string)
            
