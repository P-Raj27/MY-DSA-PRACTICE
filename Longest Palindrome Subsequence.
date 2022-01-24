#Longest Palindrome Substring by using longest common substring
string1=input()
string2=string1[::-1]
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
                    temp_maxx=array[i][j]
                    temp_maxx_i=i-1
                    temp_minn_i=temp_maxx_i+1-temp_maxx
                    temp_string=string1[temp_minn_i:temp_maxx_i+1]
                    if(temp_string==temp_string[::-1]):
                        maxx=temp_maxx
                        maxx_i=i-1
            else:
                array[i][j]=0
print(maxx)
print(maxx_i)
minn_i=maxx_i+1-maxx
print(minn_i)
print("array is=",array)
print(string1[minn_i:maxx_i+1])
