#Longest Common Substring
string1=input()
string2=input()
len1=len(string1)
len2=len(string2)
maxx=0
array=[[None]*(len2+1) for x in range(len1+1)]
for i in range(len1+1):
    for j in range(len2+1):
        if(i==0 or j==0):
            array[i][j]=0
        else:
            if(string1[i-1]==string2[j-1]):
                array[i][j]=1+array[i-1][j-1]
                
                if(array[i][j]>maxx):
                    maxx=array[i][j]
                    maxx_i=i-1
            else:
                array[i][j]=0
print(maxx)
print(maxx_i)


