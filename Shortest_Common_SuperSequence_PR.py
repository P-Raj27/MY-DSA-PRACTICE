string1=input()
string2=input()
l1=len(string1)
l2=len(string2)
array=[[None]*(l2+1) for x in range(l1+1)]
def lcs(string1,string2,l1,l2):
    for i in range(l1+1):
        for j in range(l2+1):
            if(i==0 or j==0):
                array[i][j]=0
            elif(string1[i-1]==string2[j-1]):
                array[i][j]=1+array[i-1][j-1]
            else:
                array[i][j]=max(array[i-1][j],array[i][j-1])
    return array[l1][l2]
length1=(lcs(string1,string2,l1,l2))
print(length1)
length2=len(string1+string2)
print(length2-length1)
