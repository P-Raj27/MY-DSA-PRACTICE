#Smallest window in a string containing all the characters of another string
#Smallest Window in a string to contain all the char of another string.
def satisfier(string1,string2):
    flag=0
    for i in string2:
        if(i not in string1):
            flag=1
    if(flag==0):
        return True
    else:
        return False
L=0
R=0
string1=input()
string2=input()
length1=len(string1)
length2=len(string2)
best_window_string=""
best_window_string_length=length1
while(R<length1):
    temp_string=string1[L:R+1]
    temp_length=len(temp_string)
    if(temp_length>=length2):
        if(satisfier(temp_string,string2)):
            if(temp_length<best_window_string_length):
                best_window_string=temp_string
                best_window_string_length=temp_length
            L=L+1
        else:
            R=R+1
    else:
        R=R+1
print(best_window_string)



#For Faster Solution please look at the below code,The Below Code implies Dictionary.






import collections
import sys
string1="timetopractice"
string2="toc"
R=0
L=0
#declaring counters for string2
counter_str2=collections.Counter(string2)
print("Counter_str2=",counter_str2)
counter_str1=collections.defaultdict(int)
count=0
minimum=sys.maxsize
minimum_window = ""
while(R<len(string1)):
    counter_str1[string1[R]]=counter_str1[string1[R]]+1
    if(string1[R] in counter_str2):
        if(counter_str1[string1[R]]<=counter_str2[string1[R]]):
            count=count+1
    print("count is=",count)
    while(L<=R and count==len(string2)):
        if(minimum > R-L+1):
            minimum=R-L+1
            
            minumum_window=string1[L:R+1]
            print("Minumum window-",minimum_window)
        counter_str1[string1[L]]=counter_str1[string1[L]]-1
        print(counter_str1[string1[L]],string1[L])
        if(string1[L] in counter_str2 and counter_str1[string1[L]]<counter_str2[string1[L]]):
            count=count-1
        L=L+1
    R=R+1
print(minimum_window)
