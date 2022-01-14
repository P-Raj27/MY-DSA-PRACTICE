#Longest Even Length Substring 
#This is using brute force.
def substring_Generator(string):
    '''This function will return all possible substring.'''
    substring_List=[]
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            substring_List.append(string[i:j])
    return substring_List
substring_List=substring_Generator("Pratik")
print(substring_List)
def even_Balance_Checker(substring_List):
    '''This function checks if the sum of digits is equal from both ends'''
    even_Balance_List=[]
    for i in substring_List:
        if(len(i)%2==0):
            sum1=0
            sum2=0
            for j in range(0,len(i)//2):
                sum1=sum1+int(i[j])
                sum2=sum2+int(i[len(i)-j-1])
            if(sum1==sum2):
                even_Balance_List.append(i)
    return even_Balance_List

if __name__=="__main__":
    string=input()
    maxx=0
    substring_List=substring_Generator(string)
    even_Balance_List=even_Balance_Checker(substring_List)
    for i in even_Balance_List:
        if(len(i)>maxx):
            maxx=len(i)
            maxx_element=i
    print(maxx_element)
    print(maxx)
